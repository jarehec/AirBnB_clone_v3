#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime

strptime = datetime.strptime
to_json = BaseModel.to_json


class FileStorage:
    """handles long term storage of all class instances"""
    CLS = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }
    __file_path = './dev/file.json'
    __objects = {}

    def all(self):
        """returns private attribute: __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            if not isinstance(d['created_at'], datetime):
                d['created_at'] = strptime(d['created_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
            if 'updated_at' in d:
                if not isinstance(d['updated_at'], datetime):
                    d['updated_at'] = strptime(d['updated_at'],
                                               "%Y-%m-%d %H:%M:%S.%f")
            FileStorage.__objects[o_id] = FileStorage.CLS[k_cls](**d)
