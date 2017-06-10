#!/usr/bin/python3
"""
User Place from Models Module
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class handles all application places"""

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = ''
    number_bathrooms = ''
    max_guest = ''
    price_by_night = ''
    latitude = ''
    longitude = ''
    amenity_ids = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(*args, **kwargs)
