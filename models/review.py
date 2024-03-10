#!/usr/bin/python3
"""
A module defining a class called Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """representing a class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes attributes for review """
        super().__init__(**kwargs)
