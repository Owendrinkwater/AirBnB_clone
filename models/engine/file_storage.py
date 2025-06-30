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
        """Deserialize the JSON file to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name. obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**values)
                        self.__objects[key] = instance
                except Exception:
                    pass
