#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from models import storage
import os
from werkzeug.exceptions import HTTPException


# flask setup
app = Flask(__name__)
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


def setup_errors():
    """
    This updates HTTPException Class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(Exception)
def global_error_handler(err):
    """
        Global Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
    return make_response(jsonify(message), code)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    setup_errors()
    app.run(host=host, port=port)
