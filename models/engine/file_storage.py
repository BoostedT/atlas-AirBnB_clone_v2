#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in self.all().items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    cls = models.classes[cls_name]
                    self.all()[key] = cls(**val)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """Removes an object from storage"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
                    