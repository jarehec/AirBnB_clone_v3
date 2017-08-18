#!/usr/bin/python3
import unittest
from datetime import datetime
from models import *
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
   
    def setUp(self):
        self.user = User()
        self.user.email = "bla"
        self.user.password = "bla"
        self.user.save()


    def test_all(self):
        all_objs = storage.all()
        all_user_objs = storage.all('User')

        exist_in_all = False
        for k in all_objs.keys():
            if self.user.id in k:
                exist_in_all = True
        exist_in_all_users = False
        for k in all_user_objs.keys():
            if self.user.id in k:
                exist_in_all_users = True

        self.assertTrue(exist_in_all)
        self.assertTrue(exist_in_all_users)

    def test_delete(self):
        user_id = self.user.id
        storage.delete(self.user)
        self.user = None
        storage.save()
        exist_in_all = False
        for k in storage.all().keys():
            if user_id in k:
                exist_in_all = True
        self.assertFalse(exist_in_all)

    def test_fake(self):
        print(self.user.id)



if __name__ == '__main__':
    unittest.main
