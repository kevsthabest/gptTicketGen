import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "OpenAI API Key"

def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=2072,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
    
        )
    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content

# This function listens for Get, Post and renders the response in the index.html file
@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = None

    if request.method == 'POST':
        input_text = request.form['input_text']
        issues = request.form['issues']
        os_select = request.form['os_select']

        # Send a message to the chatbot model with the input data
        message_log = [
            {"role": "system", "content": "You are a tech support agent in charge of completing support tickets, Please add missing details to the following tickets. They need to be in a bullet form and readable for laypersons Include the OS version. Can you also add a short description how  each step was performed."},
            {"role": "system", "content": "Issue: " + issues},
            {"role": "system", "content": "OS: " + os_select},
            {"role": "user", "content": input_text},
        ]  
        response = send_message(message_log)

        # Update the output_text with the response from the chatbot model
        output_text = response.strip()

    return render_template('index.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
