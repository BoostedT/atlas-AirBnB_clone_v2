#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """ Method: initialize table representing amenities"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
def __init__(self, *args, **kwargs):
    """ Initialize amenity """
    super().__init__(*args, **kwargs)