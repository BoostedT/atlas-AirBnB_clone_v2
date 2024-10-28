#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime as DATETIME
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow)
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """Deletes this BaseModel instance from the storage"""
        models.storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary['__class__'] = self.__class__.__name__
        return dictionary