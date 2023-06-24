#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_page():
    """displays webpage
    Returns:
        HTML
    """
    dict_states = storage.all(State)
    dict_amenities = storage.all(Amenity)
    all_states = []
    all_amenities = []

    for k, v in dict_states.items():
        all_states.append(v)
    for k, v in dict_amenities.items():
        all_amenities.append(v)
    return render_template('10-hbnb_filters.html', all_states=all_states,
                           all_amenities=all_amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
