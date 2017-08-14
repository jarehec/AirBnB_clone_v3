#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

now = datetime.now
strptime = datetime.strptime #takes in json string, converts to dateline object

Base = declarative_base()

class BaseModel:
    """attributes and functions for BaseModel class"""

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            id = Column(String(60), nullable=False, primary_key=True)
            created_at = Column(datetime, nullable=False, default=datetime.utcnow())

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if d['__class__']:
            d.pop('__class__')
        self.__dict__ = d

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v) #takes object, serializes to json string. Tries to serialize, return true
            return True
        except: #if unable to serialize, return false
            return False

    def bm_update(self, name, value): #updates basemodel with new or updated at attribute
        setattr(self, name, value)
        self.save()

    def save(self): #updates updated_at attribute and saves it
        """updates attribute updated_at to current time"""
        updated_at = Column(datetime, nullable=False, default=datetime.utcnow())
        models.storage.new(self)
        models.storage.save()

    def to_json(self): #conversion to json
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if k == '_sa_instance_state':
                del k
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__ #adding back in __class__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__ #class name
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def delete(self):
        """ deletes current instance from storage """
        self.delete()
