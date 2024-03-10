#!/usr/bin/python3
"""
Module that defines a class called user
"""
from models.base_model import BaseModel
from datetime import datetime
import uuid


class User(BaseModel):
    """
    class representing a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes attributes for user """
        super().__init__(**kwargs)
