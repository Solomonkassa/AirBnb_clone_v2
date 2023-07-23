#!/usr/bin/python3
"""
flask model

"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        route path
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
        C path
    """
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
        python path
    """
    return 'Python {:s}'.format(text.replace('_', ' '), strict_slashes=False)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        number path
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        template path
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
