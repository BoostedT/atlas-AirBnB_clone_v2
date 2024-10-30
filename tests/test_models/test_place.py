#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Method: Create Place test class """

    def __init__(self, *args, **kwargs):
        """ Method: constructor """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Method: test city_id-type(str) """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Method: test user_id-type(str) """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Method: test name-type(str) """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Method: test description-type(str) """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Method: test number_rooms-type(int) """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Method: test number_bathrooms-type(int) """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Method: test max_guest-type(int) """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Method: test price_by_night-type(int) """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Method: test latitude-type(float) """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Method: test longitude-type(float) """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Method: test amenity_ids-type(list) """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
