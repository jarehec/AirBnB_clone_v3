#!/usr/bin/python3
""" Database engine """

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """handles long term storage of all class instances"""
    CNC = {
	    'BaseModel': base_model.BaseModel,
            'Amenity': amenity.Amenity,
            'City': city.City,
	    'Place': place.Place,
	    'Review': review.Review,
	    'State': state.State,
	    'User': user.User
    }

    """ handles storage for database """
    __engine = None
    __session = None

    def __init__(self):
        """ creates the engine self.__engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(os.environ.get('HBNB_MYSQL_USER'), 
                                                                    os.environ.get('HBNB_MYSQL_PWD'), os.environ.get('HBNB_MYSQL_HOST'), os.environ.get('HBNB_MYSQL_DB')))
        if os.environ.get("HBNB_ENV") == 'test':
            metadata = MetaData()
            metadata.drop_all()

    def all(self, cls=None):
        """ returns a dictionary of all objects """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        obj_dict = {}
        if cls == None:
            #cls.query().all()
            for class_name in self.CNC:
#                print(class_name)
                obj_class = self.__session.query(class_name).all()
        else:                      
        #obj_dict = {}
            obj_class = self.__session.query(cls).all()
        for item in obj_class:
            obj_dict[item.id] = item
        return obj_dict
        self.__session.close()

    def new(self, obj):
        """ adds objects to current database session """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from current database session if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables in database and creates current session from engine """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
