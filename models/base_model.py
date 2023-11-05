#!/usr/bin/python3
"""
Write a class BaseModel that defines all
common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """this is the class BaseModel"""

    def __init__(self, id=uuid.uuid4()):
        """constructor"""
        self.id = str(id)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return string representation"""
        return "{} {} {}".format(
            [self.__class__.__name__], (self.id), self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        """self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__class__ = self.__class__.__name__"""
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        """new = {"__class__": self.__class__.__name__,
               "created_at": self.created_at.isoformat(),
               "updated_at": self.updated_at.isoformat()}"""
        return new
