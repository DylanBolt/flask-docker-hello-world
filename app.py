#Import necessary packages
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import logging
import json
import requests
#Intialize the flask app
app = Flask(__name__)

#Custom error handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/')
def hello():
    """This route is meant to welcome users to the flask app."""
    message = 'Welcome! Try /ping or /word. /string-counter will return the length of any string you POST to it!'
    return jsonify(message)

@app.route('/ping', methods = ['GET'])
def ping_pong():
    """This route returns a sample string in JSON."""
    return jsonify('pong!')

@app.route('/word', methods = ['GET'])
def word_reverser():
    """Reverses a random word from  https://random-word-api.herokuapp.com/word?number=1."""
    response = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    #Use .content to pull out the word from the response object!
    decoded_word = response.content.decode('utf-8')
    #Parse the word. Normally the format is ['word']
    parsed_word = decoded_word[2:-2]
    #Reverse the extracted word
    reversed_word = parsed_word[::-1]
    return jsonify(reversed_word)

@app.route('/string-count', methods = ['POST'])
def string_counter():
    """
    Expects request.get_json to return a string that we will calculate the length of.
    """
    string = request.get_json()
    length = len(string)
    return jsonify(length)
