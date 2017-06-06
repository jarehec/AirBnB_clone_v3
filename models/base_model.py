#!/usr/bin/python3
"""
Models module
"""
from uuid import uuid1
from datetime import datetime
import json


class BaseModel:
    def __init__(self):
        self.id = uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        """returns json representation of self"""
        D = dict()
        for k, v in (self.__dict__).items():
            D[k] = str(v)
        return(D)

    def __str__(self):
        return "[{:}] ({:}) {:}".format(type(self).__name__, self.id,
                                          self.__dict__)

if __name__ == '__main__':
    BaseModel
