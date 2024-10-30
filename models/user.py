#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

                                                            
class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    # when a user object is deleted, all associated place objects will be deleted.
    places = relationship("Place", backref="user", cascade="all, delete")
    # when a user object is deleted, all associated review objects will be deleted.
    reviews = relationship("Review", backref="user", cascade="all, delete")
