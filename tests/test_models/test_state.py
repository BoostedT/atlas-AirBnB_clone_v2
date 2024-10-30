#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Method: Create class for state test """

    def __init__(self, *args, **kwargs):
        """ Method: Constrcutor """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Method: test name-type(str) """
        new = self.value()
        self.assertEqual(type(new.name), str)
