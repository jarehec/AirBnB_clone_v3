#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def cities(city_id=None, state_id=None):
    """
        cities route to handle http method for requested states
    """
    all_cities = storage.all('City')

    if request.method == 'GET':
        if city_id:
            fetch_string = "{}.{}".format('City', city_id)
            city_obj = all_cities.get(fetch_string)
            if city_obj:
                return jsonify(city_obj.to_json())
            else:
                abort(404)

        else:
            all_cities = list(obj.to_json() for obj in all_cities.values()
                              if obj.state_id == state_id)
            return jsonify(all_cities)

    if request.method == 'DELETE':
        if city_id:
            fetch_string = "{}.{}".format('City', city_id)
            city_obj = all_cities.get(fetch_string)
        if city_obj:
            city_obj.delete()
            del city_obj
            return jsonify({}), 200
        abort(404)

    if request.method == 'POST':
        all_states = storage.all("States")
        fetch_state = "{}.{}".format("State", state_id)
        if all_states.get(fetch_state) is None:
            abort(404)
            req_json = request.get_json()
        if req_json is None:
            return "Not a JSON", 400
        if req_json.get("name") is None:
            return "Missing name", 400
        City = CNC.get("City")
        new_object = City(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201

    if request.method == 'PUT':
        if city_id:
            fetch_string = "{}.{}".format('City', city_id)
            city_obj = all_cities.get(fetch_string)
            req_json = request.get_json()
            if city_obj is None:
                abort(404)
            if req_json is None:
                return "Not a JSON", 400
            for name, value in req_json.items():
                city_obj.bm_update(name, value)
                return jsonify(city_obj.to_json()), 200
