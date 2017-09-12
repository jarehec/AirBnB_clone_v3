#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify, Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')


@app_views.route('/status')
def status():
    """
    function for status route that returns the status
    """
    resp = {"status": "OK"}
    return jsonify(resp)
