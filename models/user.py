#!/usr/bin/python3
"""
User Class from Models Module
"""
import hashlib
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """
        User class handles all application users
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        __encrypted_pwd = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
    else:
        email = ''
        __encrypted_pwd = ''
        first_name = ''
        last_name = ''

    @property
    def password(self):
        """
            getter: returns request to password
        """
        return self.__encrypted_pwd

    @password.setter
    def password(self, password):
        """
            setter: encrypts password to MD5
        """
        secure = hashlib.md5()
        secure.update(password.encode("utf-8"))
        secure_password = secure.hexdigest()
        self.__encrypted_pwd = secure_password
