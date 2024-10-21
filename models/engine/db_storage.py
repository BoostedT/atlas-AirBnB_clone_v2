#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ This class manages storage of hbnb models in a database """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor for DBStorage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage """
        from models import classes
        objs = {}
        if cls:
            if type(cls) == str:
                cls = classes[cls]
            for obj in self.__session.query(cls):
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for name, cls in classes.items():
                for obj in self.__session.query(cls):
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """ Adds new object to storage """
        self.__session.add(obj)

    def save(self):
        """ Saves storage to database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from storage """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads storage from database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Calls remove() on the private session attribute """
        self.__session.close()
