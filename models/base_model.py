#!/usr/bin/python3
"""
Models File with BaseModel Class
"""
import json
import models
from uuid import uuid1
from datetime import datetime


class BaseModel:
    """attributes and functions for BaseModel class"""
    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        self.id = uuid1()
        self.created_at = datetime.now()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
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
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
