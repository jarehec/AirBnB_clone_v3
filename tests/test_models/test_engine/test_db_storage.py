#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage

State = state.State
Base = base_model.Base

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ' Database engine '
        actual = db_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = ' returns a dictionary of all objects '
        actual = DBStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ' adds objects to current database session '
        actual = DBStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = ' commits all changes of current database session '
        actual = DBStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ' creates all tables in database & current session from engine '
        actual = DBStorage.reload.__doc__
        self.assertEqual(expected, actual)

    def test_doc_delete(self):
        """... documentation for delete function"""
        expected = ' deletes obj from current database session if not None '
        actual = DBStorage.delete.__doc__
        self.assertEqual(expected, actual)

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestBaseFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('......... Testing DBStorage .;.......')
        print('........ For DBStorage Class ........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new storage object for testing"""
        storage = DBStorage()
        storage.reload()
        session = storage._DBStorage__session
        self.bm_obj = Base()

    #def tearDown(self):
    #    session.remove()

    def test_instantiation(self):
        """... checks proper DBStorage instantiation"""
        self.assertIsInstance(storage, DBStorage)

    def test_new(self):
        """ test if new instance is created """
        storage.reload()
        self.assertIsNotNone(self.bm_obj)

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        actual = 0
        all_obj = storage.all()
        if bm_obj in all_obj:
            actual = 1
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        actual = 0
        all_obj = storage.all()
        if bm_obj in all_obj:
            actual = 1
        self.assertTrue(1 == actual)

@unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db', 'skip if environ is not db')
class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('.......... User  Class ..........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        storage = DBStorage()
        storage.reload()
        session = storage._DBStorage__session
        state = State(name="California")

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        actual = 0
        storage.reload()
        all_obj = storage.all()
        for k, v in all_obj.items():
            if v == state.id:
                actual = 1
        self.assertTrue(1 == actual)

if __name__ == '__main__':
    unittest.main
