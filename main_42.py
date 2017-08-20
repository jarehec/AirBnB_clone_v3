#!/usr/bin/python3
from models import *

all_places = storage.all("Place")
places_by_name = {}

for p_id in all_places.keys():
    place = all_places[p_id]
    places_by_name[place.name] = place


for p_name in sorted(places_by_name.keys()):
    place = places_by_name[p_name]
    print("place: {}".format(place.name))
    if place.amenities is None:
        continue
    amenities_names = []
    for amenity in place.amenities:
        amenities_names.append(amenity.name)
    
    for a_name in sorted(amenities_names):
        print("\tamenity: {}".format(a_name))
