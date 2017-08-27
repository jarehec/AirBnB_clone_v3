#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state_list():
    """
        method to render states
    """
    states = storage.all('State').values()
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
        method to render state ids
    """
    state_all = storage.all('State')
    try:
        state_id = state_all[id]
    except:
        state_id = None
    return render_template('9-states.html', state_id=state_id)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
