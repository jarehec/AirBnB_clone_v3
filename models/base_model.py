#!/usr/bin/python3
"""
Models module
"""
from uuid import uuid
import datetime


class BaseModel:
    def __init__(self, name="", number=0):
        self.id = uuid1()
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        self.__name = name
        self.__number = number

    @property
    def name(self):
        """return name of class instance"""
        return(self.__name)

    @name.setter
    def name(self, name):
        """setter for name atatribure"""
        self.__name = name

    @property
    def number(self):
        """return number attribute"""
        return(self.__number)

    @number.setter
    def number(self, number):
        """setter for number attribute"""
        self.__number = number

    def save(self):
        pass

    def to_json(self):
        pass

    def __str__(self):
        return "[<class name>] (<self.id>) <self.__dict__>"
