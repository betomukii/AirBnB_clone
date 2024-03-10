#!/usr/bin/python3
"""
A module that defines a class called BaseModel
"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Representing a class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        args:
            *args: list of arguments or
            length of arguments
            **kwargs: key-value arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        str representation
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        a method that updates the public instance
        attribute update_at with current datetime
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys and values
        of self.__dict__, a key __class__must be added to the
        dictionary created_at, updated_at must be converted to
        string object in ISO format
        """
        to_dictformat = {}
        # Adding a class key to identify class name
        # of the instance attribute

        to_dictformat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                to_dictformat[key] = val.isoformat()
            else:
                to_dictformat[key] = val
        return to_dictformat
