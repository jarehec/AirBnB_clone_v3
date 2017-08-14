#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class handles all application users"""

    #email = ''
    #password = ''
    #first_name = ''
    #last_name = ''
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('PLace', cascade='delete')
    reviews = relationship('Review', cascade='delete')


    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
