#!/usr/bin/python3
"""
File storage instance module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

l_classes = ['BaseModel', 'User', 'Amenity',
             'Place', 'City', 'State', 'Review']

l_cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']
