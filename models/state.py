#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(Base):
    """ State class """
    __tablename__ ='states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ Getter for cities """
        if models.storage_type == 'db':
            return self.cities
        else:
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
