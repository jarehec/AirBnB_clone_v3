#!/usr/bin/python3
""" Database engine """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base_model, amenity, city, place, review, state, user

class DBStorage:
    """ handles storage for database """
    __engine = None
    __session = None

    def init(self):
        """ creates the engine self.__engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, 
                                                                    HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
        if HBNB_ENV == 'test':
            metadata = MetaData()
            metadata.drop_all()

    def all(self, cls=None):
        """ returns a dictionary of all objects """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
#        if cls == 'None':
                               
        obj_dict = {}
        obj_class = __session.query(cls).all()
        for item in obj_class:
            obj_dict[item.id] = item
        return obj_dict
        __session.close()

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
