from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import logging

app = Flask(__name__)

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

@app.route('/ping', methods=['GET'])
def ping_pong():
    """
    return jsonify('pong!')





@app.route('/string-count', methods=['POST'])
def string-counter():
    """
    Expects request.get_json to return a string that we will calculate the length of.

    """
    response_object = {'status': 'success'}
    if request.method == 'POST':
        string = request.get_json()
        length = len(string)
        response_object['string_length'] = length
    return jsonify(response_object)



if __name__ == "__main__":
    app.run()



#returned_function = app.route('/ping', methods=['GET'])
#returned_function(ping_pong)
