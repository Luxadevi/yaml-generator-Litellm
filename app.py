from flask import Flask, render_template, request, jsonify
import yaml
import json
import os

app = Flask(__name__)

def process_provider_data(provider, form_data, provider_config):
    litellm_params = {}
    for field, field_type in provider_config.get('fields', {}).items():
        if field_type == 'checkbox':
            litellm_params[field] = field in form_data
        else:
            litellm_params[field] = form_data.get(field, provider_config.get('defaults', {}).get(field))

    return litellm_params

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('options.json', 'r') as file:
        options = json.load(file)

    if request.method == 'POST':
        form_data = request.form
        provider = form_data.get('providers')
        model_name = form_data.get('model_name')
        show_yaml = 'show_yaml' in form_data
        output_dir = form_data.get('output_dir', '')

        provider_config = options['providers'].get(provider, {})
        litellm_params = process_provider_data(provider, form_data, provider_config)

        config_data = {
            "model_list": [
                {
                    "model_name": model_name,
                    "litellm_params": litellm_params
                }
            ]
        }

        yaml_data = yaml.dump(config_data, default_flow_style=False, sort_keys=False)

        if show_yaml:
            return jsonify({'yaml': yaml_data})
        else:
            file_name = 'config.yaml'
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
