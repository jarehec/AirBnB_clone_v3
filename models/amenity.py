#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
from models.place import PlaceAmenity

class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('PlaceAmenity', secondary=place_amenity, backref='amenities', cascade='delete')

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs) #refers to most direct parent, BaseModel
