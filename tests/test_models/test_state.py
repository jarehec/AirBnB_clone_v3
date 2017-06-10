#!/usr/bin/python3
"""
Unit Test for State Class
"""
import unittest
from datetime import datetime
import models
import json

State = models.state.State
BaseModel = models.base_model.BaseModel


class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new state'
        actual = State.__init__.__doc__
        self.assertEqual(expected, actual)


class TestStateInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  State Class  .........')
        print('.................................\n\n')

    def test_instantiation(self):
        """... checks if State is properly instantiated"""
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_state = State()
        my_str = str(my_state)
        my_list = ['State', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_state = State()
        my_str = str(my_state)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        my_state = State()
        my_state.save()
        actual = type(my_state.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_state = State()
        my_state_json = my_state.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_state_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value State"""
        my_state = State()
        my_state_json = my_state.to_json()
        actual = None
        if my_state_json['__class__']:
            actual = my_state_json['__class__']
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        my_state = State()
        my_state.name = "betty"
        if hasattr(my_state, 'name'):
            actual = my_state.name
        else:
            acual = ''
        expected = "betty"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
