#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from api.v1.views import app_views
from flask import Flask, jsonify, render_template, url_for
from models import storage
import os


# flask setup
app = Flask(__name__)
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """
        Route to handle 404 status Page Not Found
    """
    resp = {"error": "Not found"}
    return jsonify(resp), 404

if __name__ == "__main__":
    """
    MAIN Flask App
    """
    app.run(host=host, port=port)
