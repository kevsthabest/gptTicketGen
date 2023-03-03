# Flask Chatbot for Tech Support Tickets

This is a Flask-based chatbot that interacts with OpenAI's GPT-3 model to respond to tech support tickets. Users can input a description of an issue and the operating system in use, and the chatbot will respond with a set of instructions for how to resolve the issue.

## Getting Started

### Prerequisites

To run the Flask app, you will need Python 3 installed on your system. You will also need to install the required packages by running:



`pip install -r requirements.txt`

### Setting up the OpenAI API Key

To use OpenAI's GPT-3 model, you will need to sign up for an API key [here](https://beta.openai.com/signup/). Once you have your API key, you can set it in the `app.py` file:



`openai.api_key = "YOUR_API_KEY"`

### Running the Flask App

To run the Flask app, navigate to the project directory in your terminal and run:



`python app.py`

This will start the Flask app on your local machine. You can access the app by navigating to [http://localhost:5000](http://localhost:5000/) in your web browser.

## Usage

To use the chatbot, input a description of an issue in the "Input Text" field and select the operating system in use from the dropdown menu. Then click "Submit" to send the message to the chatbot. The chatbot will respond with a set of instructions for how to resolve the issue.

## Built With

-   Flask - a lightweight WSGI web application framework
-   OpenAI - a research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc.

## Authors

-   [Kevin Legacy-Aube](https://github.com/kevsthabest)

## Acknowledgments

-   This project was inspired by the [OpenAI chatbot example](https://beta.openai.com/examples/inputs-outputs/1).
