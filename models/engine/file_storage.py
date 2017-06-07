#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON
"""
import json
from models.base_model import BaseModel
to_json = BaseModel.to_json


class FileStorage:
    """serializes to JSON file and deserializes JSON file to instance"""
    def __init__(self):
        """instantiation of new FileStorage class instance"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """returns private attribute: __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        o_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[o_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = self.__file_path
        o_d = dict([k, v.to_json()] for k, v in self.__objects.items())
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(o_d, f_io)
            f_io.close()

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = self.__file_path
        with open(fname, mode='r', encoding='utf-8') as f_io:
            self.__objects = json.load(f_io)
            f_io.close()
        pass
