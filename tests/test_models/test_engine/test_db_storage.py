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
City = city.City
Base = base_model.BaseModel
DBStorage = engine.db_storage.DBStorage
storage = storage

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
class TestBaseBDInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('......... Testing DBStorage .;.......')
        print('........ For DBStorage Class ........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new storage object for testing"""
        storage._DBStorage__session.close()
        dbs = DBStorage()
        session = dbs._DBStorage__session
        self.bm_obj = Base()

    def tearDown(self):
        self.session.remove()
        DBStorage.session.close()

    def test_instantiation(self):
        """... checks proper DBStorage instantiation"""
        self.assertIsInstance(self.storage, DBStorage)

    def test_new(self):
        """ test if new instance is created """
        self.storage.reload()
        self.assertIsNotNone(self.bm_obj)

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        all_obj = storage.all()
        actual = 0
        if bm_obj in all_obj:
            actual = 1
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        s = State(**{"name": "Calfornia"})

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
        self.user = User()
        self.bm_obj = BaseModel()

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        u_id = self.user.id
        all_obj = storage.all()
        actual = 0
        for k in all_obj.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_new(self):
        """ test if new instance is created """
        s = State(name="California")
        self.store()
        all_obj = storage.all()
        s.save()
        self.reload()
        self.assertEqual(s.save(), self.reload())

if __name__ == '__main__':
    unittest.main
