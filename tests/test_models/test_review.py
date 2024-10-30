#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Method: Create class for review test """

    def __init__(self, *args, **kwargs):
        """ Method: Constructor """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Method: Test place_id-type(str) """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Method: Test user_id-type(str) """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Method: Test text-type(str) """
        new = self.value()
        self.assertEqual(type(new.text), str)
