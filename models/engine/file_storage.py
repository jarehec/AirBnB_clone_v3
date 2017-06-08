#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON
"""
import json
from ..base_model import BaseModel
to_json = BaseModel.to_json


class FileStorage:
    """serializes to JSON file and deserializes JSON file to instance"""
    def __init__(self):
        """instantiation of new FileStorage class instance"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def delete(self, key):
        """destroys an instance and updates the storage file"""
        del self.__objects[key]
        self.save()

    def all(self):
        """returns private attribute: __objects"""
        return self.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = self.__file_path
        d = {}
        for bm_id, bm_obj in self.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = self.__file_path
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objects = json.load(f_io)
            for bm_id, obj_dict in new_objects.items():
                if 'BaseModel' in bm_id:
                    self.__objects[bm_id] = BaseModel(**obj_dict)
        except:
            pass
