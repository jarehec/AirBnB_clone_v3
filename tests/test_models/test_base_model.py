#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from models.base_model import BaseModel

save = BaseModel.save
to_json = BaseModel.to_json


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel"""
    def test_instantiation(self):
        """Test for successful instantiation"""
        my_model = BaseModel()
        self.assertEqual(str(my_model)[:11], "[BaseModel]")

if __name__ == '__main__':
    unittest.main
