#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class handles all application reviews"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
