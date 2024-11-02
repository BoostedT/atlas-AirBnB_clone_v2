#!/usr/bin/python3
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models
from models import storage
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ Getter for cities """
        if storage.__class__.__name__ != 'DBStorage':
            return [city for city in storage.all(City).values() if city.state_id == self.id]
        return []
