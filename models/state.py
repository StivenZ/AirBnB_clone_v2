#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_STORAGE') == 'db':
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            """ Adds every instance of City and returns a list """
            cities_dict = models.storage.all(City)
            cities_list = []
            for value in cities_dict.values():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_list
