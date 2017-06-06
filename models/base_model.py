#!/usr/bin/python3
"""
Models File with BaseModel Class
"""
import uuid
import json
from datetime import datetime


class BaseModel:
    def __init__(self):
        """instantiation of new BaseModel Class"""
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = datetime.now()

    def is_serializable(self, obj_x):
        """checks if object is serializable"""
        try:
            json.dumps(obj_x)
            return True
        except:
            return False

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = self.__class__.__name__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        return "[{:}] ({:}) {:}".format(type(self).__name__, self.id,
                                        self.__dict__)
