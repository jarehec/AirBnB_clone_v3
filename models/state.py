#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class handles all application states"""

    #name = ''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('Cities', cascade='delete')

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
