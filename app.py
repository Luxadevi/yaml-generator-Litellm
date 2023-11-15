from flask import Flask, render_template, request
import yaml
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('options.json', 'r') as file:
        options = json.load(file)

    if request.method == 'POST':
        form_data = request.form
        model_name = form_data.get('model_name')
        api_base = form_data.get('api_base')
        stream = 'stream' in form_data

        litellm_params = {
            "model": model_name,
            "api_base": api_base
        }
        if stream:
            litellm_params["stream"] = True

        config_data = {
            "model_list": [
                {
                    "model_name": model_name,
                    "litellm_params": litellm_params
                }
            ]
        }

        # Write to YAML file
        with open('config.yaml', 'w') as file:
            yaml.dump(config_data, file, default_flow_style=False, sort_keys=False)

        # Redirect or notify user of success
        # ...

    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)
