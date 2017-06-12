#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class handles all application cities"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
