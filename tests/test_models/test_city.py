#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Method: Create city test class """

    def __init__(self, *args, **kwargs):
        """ Method: constructor """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Method: Verify state_id-type(str)"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Method: Verify name-type(str)"""
        new = self.value()
        self.assertEqual(type(new.name), str)
