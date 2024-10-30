#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Method: Create class for user test """

    def __init__(self, *args, **kwargs):
        """ Method: Constructor """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Method: Test first_name-type(str) """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Method: Test last_name-type(str) """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Method: Test email-type(str) """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Method: Test password-type(str) """
        new = self.value()
        self.assertEqual(type(new.password), str)
