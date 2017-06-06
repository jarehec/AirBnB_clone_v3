#!/usr/bin/python3
"""
Models module
"""
from uuid import uuid1
from datetime import datetime
import json


class BaseModel:
    def __init__(self, name="", my_number=0):
        self.id = uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.__name = name
        self.__my_number = my_number


    @property
    def name(self):
        """return name of class instance"""
        return(self.__name)

    @name.setter
    def name(self, name):
        """setter for name atatribure"""
        self.__name = name

    @property
    def my_number(self):
        """return my_number attribute"""
        return(self.__my_number)

    @my_number.setter
    def my_number(self, my_number):
        """setter for number attribute"""
        self.__my_number = my_number


    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        """returns json representation of self"""
        return(self.__dict__)

    def __str__(self):
        return "[{:}] ({:}) {:}".format(type(self).__name__, self.id,
                                          self.__dict__)

if __name__ == '__main__':
    BaseModel
