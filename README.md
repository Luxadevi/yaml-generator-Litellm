# LiteLLM Config Generator

## Overview

LiteLLM Config Generator is a web-based tool designed to simplify the process of generating YAML configuration files for various language model providers like Huggingface, Palm API, and AWS Bedrock. This tool allows users to dynamically add configurations for different providers and generate a consolidated YAML file that can be used to configure language models in a standardized format.

## Features

- Dynamic form generation based on selected language model providers.
- Support for multiple providers including Huggingface, Palm API, and AWS Bedrock.
- Option to display generated YAML on-screen for quick review.
- Customizable configurations for each provider.
- Easy-to-use web interface.

## Installation

To set up the LiteLLM Config Generator on your local machine, follow these steps:

1. **Clone the Repository:**

```bash
git clone https://github.com/Luxadevi/yaml-generator-Litellm
cd yaml-generator-Litellm/
``` 

2. **Install Dependencies:**
Ensure you have Python installed on your system. Then, install the required Python packages:

```bash
pip install flask pyyaml
```

3. **Run the Application:**

```bash
python app.py
```

This will start the Flask server, and the application should now be accessible at http://localhost:5000.

## Usage

After starting the application, navigate to http://localhost:5000 in your web browser. Follow these steps to generate a YAML configuration:

1. Select a language model provider from the dropdown menu.
2. Fill in the required fields for the selected provider.
3. Optionally, add more configurations by clicking the "Add Next" button.
4. Click "Generate YAML" to view the generated configuration.
5. If you want to download the YAML file, uncheck the "Only Show Generated YAML" checkbox before generating.

## Contributing

Contributions to the LiteLLM Config Generator are welcome! If you have suggestions for improvements or want to contribute to the code, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Please ensure your code adheres to the project's coding standards and include tests for new features.
