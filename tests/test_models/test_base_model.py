#!/usr/bin/python3
""" Module that tests all BaseModel methods and attributes """

import os
import json
import unittest
import datetime
from models.base_model import BaseModel
from uuid import UUID


class test_basemodel(unittest.TestCase):
    """ class that tests methods of BaseModel """

    def __init__(self, *args, **kwargs):
        """ constructor for test_basemodel class """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ """
        obj = self.value()
        self.assertEqual(type(obj), self.value)

    def test_kwargs(self):
        """ """
        obj = self.value()
        copy = obj.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is obj)

    def test_kwargs_int(self):
        """ """
        obj = self.value()
        copy = obj.to_dict()
        new = copy.update({1: 2})
        self.assertRaises(TypeError)

    def test_save(self):
        """ test save method """
        obj = self.value()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as file:
            json_format = json.load(file)
            self.assertEqual(json_format[key], obj.to_dict())

    def test_str(self):
        """ test string method """
        obj = self.value()
        self.assertEqual(str(obj), f'{self.name} {obj.id} {obj.__dict__}')

    def test_todict(self):
        """ test for to_dict method """
        obj = self.value()
        dict_obj = obj.to_dict()
        self.assertEqual(obj.to_dict(), dict_obj)

    def test_kwargs_none(self):
        """ test against correct arguments type"""
        arg = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**arg)

    def test_kwargs_one(self):
        """ test against correct key """
        arg = {'Name': 'test'}
        new = self.value(**arg)
        self.assertRaises(KeyError)

    def test_id(self):
        """ test id's attribute type """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created_at attribute type """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test updated_at attribute type"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
