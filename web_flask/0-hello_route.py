#!/usr/bin/python3
"""class Flask"""
from flask import Flask
"""class Flask"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays text
    Returns:
        text
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
