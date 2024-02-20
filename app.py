from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import time

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY", 'your_default_api_key')

# Define the impersonated role with instructions
impersonated_role = """
    As Dr. AI, assist patients in Arabic with symptom checking, medication details, treatment options, finding doctors and hospitals, and scheduling appointments.
   Be friendly and knowledgeable. Only answer medical questions; respond with "I don't know" for non-medical queries.
   Prioritize patient privacy, use Arabic, and create an enjoyable and informative healthcare experience.
"""

# Initialize variables for chat history
explicit_input = ""
chatgpt_output = 'Chat log: /n'
cwd = os.getcwd()
i = 1

# Find an available chat history file
while os.path.exists(os.path.join(cwd, f'chat_history{i}.txt')):
    i += 1

history_file = os.path.join(cwd, f'chat_history{i}.txt')

# Create a new chat history file
with open(history_file, 'w') as f:
    f.write('\n')

# Initialize chat history
chat_history = ''

# Create a Flask web application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, impersonated_role, explicit_input, chat_history):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Conversation history: {chat_history}"},
            {"role": "user", "content": f"{user_input}. {explicit_input}"},
        ]
    )

    for item in output['choices']:
        chatgpt_output = item['message']['content']

    return chatgpt_output

name = ' bot'

# Function to handle user chat input
def chat(user_input):
    global chat_history, name, chatgpt_output
    current_day = time.strftime("%d/%m", time.localtime())
    current_time = time.strftime("%H:%M:%S", time.localtime())
    chat_history += f'\nUser: {user_input}\n'
    chatgpt_raw_output = chatcompletion(user_input, impersonated_role, explicit_input, chat_history).replace(f'{name}:', '')
    chatgpt_output = f'{name}: {chatgpt_raw_output}'
    chat_history += chatgpt_output + '\n'
    with open(history_file, 'a') as f:
        f.write('\n'+ current_day+ ' '+ current_time+ ' User: ' +user_input +' \n' + current_day+ ' ' + current_time+  ' ' +  chatgpt_output + '\n')
        f.close()
    return chatgpt_raw_output

# Flask route to handle chat requests
def get_response(userText):
    return chat(userText)

# API endpoint for the bot response
@app.route("/api/get_response", methods=["POST"])
def api_get_response():
    try:
        user_text = request.json.get('msg')
        response = get_response(user_text)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)