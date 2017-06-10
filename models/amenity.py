#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class handles all application amenities"""

    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new instance of Amenity"""
        super().__init__(*args, **kwargs)
