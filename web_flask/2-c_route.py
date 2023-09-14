#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, escape

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Define a route for "/hbnb" with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Define a route for "/c/<text>" with strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces and return the result
    text = escape(text).replace('_', ' ')
    return 'C ' + text

# Run the application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
