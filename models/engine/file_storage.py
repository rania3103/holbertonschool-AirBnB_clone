#!/usr/bin/python3
"""Write a class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances"""
import json
from models.base_model import BaseModel


class FileStorage:
    """this is the class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            dict = {}
            for k, v in self.__objects.items():
                dict[k] = v.to_dict()
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
                for k, v in dict.items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except FileNotFoundError:
            pass
