from flask import Flask, render_template, request, jsonify
import yaml
import json
import os

app = Flask(__name__)

def process_provider_data(provider, form_data, provider_config, config_number):
    litellm_params = {}
    for fieldObj in provider_config.get('fields', []):
        field = list(fieldObj.keys())[0]  # Get the field name
        field_type = fieldObj[field]

        form_field_name = f"{field}-{config_number}"
        if field_type == 'checkbox':
            litellm_params[field] = form_field_name in form_data
        elif isinstance(field_type, dict) and field_type.get('type') == 'select':
            # Handle dropdown selections
            litellm_params[field] = form_data.get(form_field_name, provider_config.get('defaults', {}).get(field))
        else:
            litellm_params[field] = form_data.get(form_field_name, provider_config.get('defaults', {}).get(field))

    # Apply default values if not present
    for key, value in provider_config.get('defaults', {}).items():
        if key not in litellm_params:
            litellm_params[key] = value

    # Special handling for the huggingface provider
    if provider == "huggingface":
        user = form_data.get(f'user-{config_number}', '')
        model = form_data.get(f'model-{config_number}', '')
        litellm_params['model'] = f"huggingface/{user}/{model}" if user and model else model

    return litellm_params

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('options.json', 'r') as file:
        options = json.load(file)

    if request.method == 'POST':
        form_data = request.form
        show_yaml = 'show_yaml' in form_data
        config_count = int(form_data.get('config_count', 1))

        config_data = {"model_list": []}

        # Process each configuration
        for i in range(1, config_count + 1):
            provider = form_data.get(f'providers-{i}')
            model_name = form_data.get(f'model_name-{i}')
            provider_config = options['providers'].get(provider, {})
            litellm_params = process_provider_data(provider, form_data, provider_config, i)

            config_data["model_list"].append({
                "model_name": model_name,
                "litellm_params": litellm_params
            })

        yaml_data = yaml.dump(config_data, default_flow_style=False, sort_keys=False)

        if show_yaml:
            return jsonify({'yaml': yaml_data})
        else:
            file_name = 'config.yaml'
            output_dir = form_data.get('output_dir', '')
            if output_dir:
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                file_path = os.path.join(output_dir, file_name)
            else:
                file_path = file_name

            with open(file_path, 'w') as file:
                file.write(yaml_data)

    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
