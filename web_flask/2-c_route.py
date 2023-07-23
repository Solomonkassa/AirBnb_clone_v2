#!/usr/bin/python3
"""
flask model
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        / home path
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index():
    """
        /hbnb path
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    """
        /C path
    """
    return 'C {:s}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
