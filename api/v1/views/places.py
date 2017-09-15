#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def places_per_city(city_id=None):
    """
        places route to handle http method for requested places by city
    """
    city_obj = storage.get('City', city_id)

    if request.method == 'GET':
        if city_obj is None:
            abort(404, 'Not found')
        all_places = storage.all('Place')
        city_places = [obj.to_json() for obj in all_places.values()
                       if obj.city_id == city_id]
        return jsonify(city_places)

    if request.method == 'POST':
        if city_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        user_id = req_json.get("user_id")
        if user_id is None:
            abort(400, 'Missing user_id')
        user_obj = storage.get('User', user_id)
        if user_obj is None:
            abort(404, 'Not found')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        Place = CNC.get("Place")
        req_json['city_id'] = city_id
        new_object = Place(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'])
def places_with_id(place_id=None):
    """
        places route to handle http methods for given place
    """
    place_obj = storage.get('Place', place_id)

    if request.method == 'GET':
        if place_obj is None:
            abort(404, 'Not found')
        return jsonify(place_obj.to_json())

    if request.method == 'DELETE':
        if place_obj is None:
            abort(404, 'Not found')
        place_obj.delete()
        del place_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        if place_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        place_obj.bm_update(req_json)
        return jsonify(place_obj.to_json()), 200


@app_views.route('/places_search', methods=['POST'])
def places_search(city_id=None):
    """
        places route to handle http method for request to search places
    """
    all_places = storage.all('Place')

    req_json = request.get_json()
    if req_json is None:
        return jsonify([
            place.to_json() for place in all_places.values()
        ])
    states = req_json.get('states')
    if states and len(states) > 0:
        all_states = [
            storage.get('State', s_id) for s_id in states
        ]
        all_cities = storage.all('City')
        state_cities = [
            city for city in all_cities.values() if city.state_id in all_states
        ]
    else:
        state_cities = None
    cities = req_json.get('cities')
    if cities and len(cities) > 0:
        city_objs = [
            storage.get('City', c_id) for c_id in cities
        ]
    else:
        city_objs = None
    if state_cities and city_objs:
        cities = state_cities
        for city in city_objs:
            if city not in state_cities:
                cities.append(city)
    elif state_cities:
        cities = state_cities
    elif city_objs:
        cities = city_objs
    else:
        cities = None
    amenities = req_json.get('amenities')
    if amenities and cities:
        return jsonify([
        ])
    if amenities is None and cities is None:
        return jsonify([
            place.to_json() for place in all_places.values()
        ])
    if cities and amenities is None:
        return jsonify([
            place.to_json() for place in all_places.values()
            if place.city_id in cities
        ])
    if amenities and cities is None:
        return jsonify([
            place.to_json() for place in all_places.values()
        ])
