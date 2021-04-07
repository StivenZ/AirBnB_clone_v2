#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            """ Adds every instance of City and returns a list """
            from models import storage
            cities_dict = storage.all(City)
            cities_list = []
            for value in cities_dict.values():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_list
