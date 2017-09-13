#!/usr/bin/python3
"""
    Flask route that returns json respone
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC


@app_views.route('/amenities/')
@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenities(amenity_id=None):
    """
        amenities route that handles http requests
    """
    all_amenities = storage.all('Amenity')
    fetch_string = "{}.{}".format('Amenity', amenity_id)
    amenity_obj = all_amenities.get(fetch_string)

    if request.method == 'GET':
        if amenity_obj:
            return jsonify(amenity_obj.to_json())
        else:
            abort(404, 'Not found')

    if request.method == 'DELETE':
        if amenity_obj:
            amenity_obj.delete()
            del amenity_obj
            return jsonify({}), 200
        else:
            abort(404, 'Not found')

    if request.method == 'POST':
        if amenity_obj:
            req_json = request.get_json()
            if req_json is None:
                abort(400, 'Not a JSON')
            if req_json.get('name') is None:
                abort(400, 'Missing name')
            Amenity = CNC.get('Amenity')
            new_object = Amenity(**req_json)
            new_object.save()
            return jsonify(new_object.to_json()), 201
        else:
            abort(404, 'Not found')

    if request.method == 'PUT':
        if amenity_obj:
            req_json = request.json()
            if amenity_obj is None:
                abort(404, 'Not found')
            if req_json is None:
                abort(400, 'Not a JSON')
            amenity_obj.bm_update(req_json)
            return jsonify(amenity_obj.to_json()), 200
        else:
            abort(404, 'Not found')
