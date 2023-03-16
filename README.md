# Power Virtual Agents ChatGPT

This repository contains the code for a chatbot built using the OpenAI GPT-3.5 language model. The chatbot is integrated with Power Virtual Agents, a low-code chatbot platform provided by Microsoft.

## Repository Contents

The repository contains the following files:

- `openai_module.py`: This module contains the necessary functions to interact with the OpenAI GPT-3.5 language model. 
- `app.py`: This is a Flask app that exposes endpoints to the OpenAI GPT-3.5 language model. 

## Usage

To use the chatbot, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Set up your OpenAI API credentials by creating a `.env` file in the root directory of the repository and adding your credentials in the following format: `OPENAI_API_KEY=<your_api_key>`.
4. Start the Flask app by running `python app.py`.
5. The chatbot is now accessible at `http://localhost:5000`.

## Contributing

If you find a bug or have a suggestion for improvement, please open an issue in this repository. Pull requests are also welcome.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more information.
