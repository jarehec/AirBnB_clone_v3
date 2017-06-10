#!/usr/bin/python3
"""
Unit Test for Amenity Class
"""
import unittest
from datetime import datetime
import models
import json

Amenity = models.amenity.Amenity
BaseModel = models.base_model.BaseModel


class TestAmenityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Amenity  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new amenity'
        actual = Amenity.__init__.__doc__
        self.assertEqual(expected, actual)


class TestAmenityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Amenity  Class  .........')
        print('.................................\n\n')

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_amenity = Amenity()
        my_str = str(my_amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_amenity = Amenity()
        my_str = str(my_amenity)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        my_amenity = Amenity()
        my_amenity.save()
        actual = type(my_amenity.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_amenity = Amenity()
        my_amenity_json = my_amenity.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_amenity_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value Amenity"""
        my_amenity = Amenity()
        my_amenity_json = my_amenity.to_json()
        actual = None
        if my_amenity_json['__class__']:
            actual = my_amenity_json['__class__']
        expected = 'Amenity'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        my_amenity = Amenity()
        my_amenity.name = "greatWifi"
        if hasattr(my_amenity, 'name'):
            actual = my_amenity.name
        else:
            actual = ''
        expected = "greatWifi"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
