#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models.base_model

BaseModel = models.base_model.BaseModel
is_serializable = BaseModel.is_serializable


class TestBaseModelDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""
    def test_doc_file(self):
        """Test: documentation for the file"""
        expected = '\nModels File with BaseModel Class\n'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """Test: documentation for the class"""
        expected = 'attributes and functions for BaseModel class'
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """Test: documentation for init function"""
        expected = 'instantiation of new BaseModel Class'
        actual = BaseModel.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """Test: documentation for save function"""
        expected = 'updates attribute updated_at to current time'
        actual = BaseModel.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_to_json(self):
        """Test: documentation for to_json function"""
        expected = 'returns json representation of self'
        actual = BaseModel.to_json.__doc__
        self.assertEqual(expected, actual)

    def test_doc_str(self):
        """Test: documentation for to str function"""
        expected = 'returns string type representation of object instance'
        actual = BaseModel.__str__.__doc__
        self.assertEqual(expected, actual)


class TestBaseModelInstances(unittest.TestCase):
    """testing for class instances"""
    def test_instantiation(self):
        """Test: checks proper BaseModel instantiation"""
        my_model = BaseModel()
        my_str = str(my_model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        expected = 3
        self.assertEqual(expected, actual)

    def test_instantiation_no_updated(self):
        """Test: should not have updated attribute"""
        my_model = BaseModel()
        my_str = str(my_model)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        expected = 0
        self.assertEqual(expected, actual)

    def test_save(self):
        """Test: save function should add updated_at attribute"""
        my_model = BaseModel()
        my_model.save()
        actual = type(my_model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """Test: to_json should return dictionary object that is serializable"""
        my_model = BaseModel()
        my_model_json = my_model.to_json()
        actual = 1
        for v in my_model_json.values():
            if not is_serializable(my_model, v):
                actual = 0
        expected = 1
        self.assertEqual(expected, actual)

    def test_json_class(self):
        """Test: to_json should include class key with value BaseModel"""
        my_model = BaseModel()
        my_model_json = my_model.to_json()
        actual = None
        if my_model_json['__class__']:
            actual = my_model_json['__class__']
        expected = 'BaseModel'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """Test: add name attribute"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        actual = my_model.name
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_number_attribute(self):
        """Test: add number attribute"""
        my_model = BaseModel()
        my_model.number = 98
        actual = my_model.number
        expected = 98
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
