#!/usr/bin/python3
"""
Models module
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        """returns json representation of self"""
        D = dict()
        for k, v in (self.__dict__).items():
            if (isinstance(v, (datetime, uuid.UUID))):
                D[k] = str(v)
            else:
                D[k] = v
        D["__class__"] = self.__class__.__name__
        return(D)

    def __str__(self):
        return "[{:}] ({:}) {:}".format(type(self).__name__, self.id,
                                          self.__dict__)

if __name__ == '__main__':
    BaseModel
