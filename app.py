# Import the necessary libraries
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
import flask
from openai_module import generate_chatgpt_response, summarise_youtube_video


# Create a Flask instance
app = flask.Flask(__name__)

# Create a route to the home page
@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    request_data = request.get_json()
    query = str(request_data['query'])
    response = generate_chatgpt_response(query)
    return jsonify({'response': response})

@app.route('/summarise_yt_url', methods=['POST'])
def summarise_yt_url():
    request_data = request.get_json()
    url = str(request_data['url'])
    response = summarise_youtube_video(url)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()