#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """
    function for status route that returns the status
    """
    resp = {"status": "OK"}
    return jsonify(resp)
