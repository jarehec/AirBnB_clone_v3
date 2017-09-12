#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC


@app_views.route('/states', methods=['GET', 'POST'])
@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def states(state_id=None):
    """
        states route to handle http method for requested state/s
    """
    if request.method == 'GET':
        all_states = storage.all('State')
        if state_id:
            fetch_string = "{}.{}".format('State', state_id)
            state_obj = all_states.get(fetch_string)
            if state_obj:
                return jsonify(state_obj.to_json())
            else:
                abort(404)
        else:
            all_states = list(obj.to_json() for obj in all_states.values())
            return jsonify(all_states)
    if request.method == 'DELETE':
        if state_id:
            all_states = storage.all('State')
            state_obj = all_states.get(fetch_string)
            if state_obj:
                del state_obj
                return jsonify({})
        abort(404)
    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            return "Not a JSON", 400
        if req_json.get("name") is None:
            return "Missing name", 400
        State = CNC.get("State")
        new_object = State(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201
    if request.method == 'PUT':
        all_states = storage.all('State')
        fetch_string = "{}.{}".format('State', state_id)
        state_obj = all_states.get(fetch_string)
        req_json = request.get_json()
        if state_obj is None:
            abort(404)
        if req_json is None:
            return "Not a JSON", 400
        for name, value in req_json.items():
            state_obj.bm_update(name, value)
        return jsonify(state_obj.to_json())
