#!/usr/bin/python3
"""
Module that defines a class called Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class representing a Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes attributes for amenities """
        super().__init__(**kwargs)
