#!/usr/bin/python3
"""
Module that defines a class called City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class representing a City
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes attributes for city """
        super().__init__(**kwargs)
