#!/usr/bin/python3
"""
Write a class BaseModel that defines all
common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """this is the class BaseModel"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        from models import storage

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
          updated_at with the current datetime"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new
