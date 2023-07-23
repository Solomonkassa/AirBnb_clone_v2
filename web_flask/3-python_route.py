#!/usr/bin/python3
"""
flask model

"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index():
    """
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    """
    """
    return 'C is {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    """
    return 'Python {:s}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
