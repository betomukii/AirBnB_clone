#!/usr/bin/python3
"""
Module that defines a class called state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class representing a State
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes attributes for state """
        super().__init__(**kwargs)
