#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def show_page():
    """displays webpage
    Returns:
        HTML
    """
    dict_states = storage.all(State)
    dict_amenities = storage.all(Amenity)
    dict_places = storage.all(Place)
    all_states = []
    all_amenities = []
    all_places = []

    for k, v in dict_states.items():
        all_states.append(v)
    for k, v in dict_amenities.items():
        all_amenities.append(v)
    for k, v in dict_places.items():
        all_places.append(v)
    return render_template('100-hbnb.html', all_states=all_states,
                           all_amenities=all_amenities, all_places=all_places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
