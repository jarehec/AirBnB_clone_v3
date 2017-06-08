#!/usr/bin/python3
"""
Models Module, BaseModel Class
"""

import json
import models
from uuid import uuid4, UUID
from datetime import datetime

now = datetime.now
strptime = datetime.strptime


class BaseModel:
    """attributes and functions for BaseModel class"""
    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        elif args:
            pass
        else:
            self.id = str(uuid4())
            self.created_at = now()
            models.storage.new(self)

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if 'id' in d:
            self.id = d['id']
        else:
            self.id = str(uuid4())
        if 'created_at' in d:
            if not isinstance(d['created_at'], datetime):
                setattr(self, 'created_at',
                        strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f"))
            else:
                self.created_at = d['created_at']
        else:
            self.created_at = now()
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                setattr(self, 'updated_at',
                        strptime(d['updated_at'], "%Y-%m-%d %H:%M:%S.%f"))
            else:
                self.updated_at = d['updated_at']

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = self.__class__.__name__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
