#!/usr/bin/python3
"""
User Class from Models Module
"""

from models

BaseModel = models.base_model.BaseModel

class User(BaseModel):
    """User class handles all application users"""

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        if kwargs:
            self.email = kwargs['email']
            self.password = kwargs['password']
            self.first_name = kwargs['first_name']
            self.last_name = kwargs['last_name']
        else:
            pass

