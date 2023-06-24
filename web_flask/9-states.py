#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_all_states():
    """lists states from database
    Returns:
        HTML
    """
    dict_states = storage.all(State)
    all_states = []
    for k, v in dict_states.items():
        all_states.append(v)
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def find_state(id):
    """lists states from database with specific id
    Args:
        id (str): id
    Returns:
        HTML
    """
    dict_states = storage.all(State)
    all_states = []
    all_states_id = []
    for k, v in dict_states.items():
        all_states_id.append(v.id)
        all_states.append(v)
    return render_template('9-states.html', all_states=all_states,
                           all_states_id=all_states_id, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
