#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float


class User(BaseModel, Base):
    """User class handles all application users"""
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        
        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''


    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
