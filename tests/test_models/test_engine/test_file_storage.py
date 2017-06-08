#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
import json

BaseModel = models.base_model.BaseModel
FileStorage = models.file_storage.FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = models.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiation of new FileStorage class instance'
        actual = FileStorage.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = 'returns private attribute: __objects'
        actual = FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ("sets / updates in __objects the obj with key <obj class "
                    "name>.id")
        actual = FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = 'serializes __objects to the JSON file (path: __file_path)'
        actual = FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ("if file exists, deserializes JSON file to __objects, "
                    "else nothing")
        actual = FileStorage.reload.__doc__
        self.assertEqual(expected, actual)

class TestBaseModelInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_instantiation(self):
        """... checks proper BaseModel instantiation"""
        my_model = BaseModel()
        my_str = str(my_model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_model = BaseModel()
        my_str = str(my_model)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_save(self):
        """... save function should add updated_at attribute"""
        my_model = BaseModel()
        my_model.save()
        actual = type(my_model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_model = BaseModel()
        my_model_json = my_model.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_model_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value BaseModel"""
        my_model = BaseModel()
        my_model_json = my_model.to_json()
        actual = None
        if my_model_json['__class__']:
            actual = my_model_json['__class__']
        expected = 'BaseModel'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        actual = my_model.name
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_number_attribute(self):
        """... add number attribute"""
        my_model = BaseModel()
        my_model.number = 98
        actual = my_model.number
        self.assertTrue(98 == actual)

if __name__ == '__main__':
    unittest.main
