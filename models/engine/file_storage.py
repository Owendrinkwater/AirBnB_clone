#!/usr/bin/python3
# models/engine/file_storage.py

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes instances to/from a JSON file"""
    __file_path = "db.t:xt"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the to the JSON file."""
        obj_dict = {
             key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
