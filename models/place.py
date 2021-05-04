#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, Float, Table
from sqlalchemy import MetaData
metadata = Base.metadata


place_amenity = Table('place_amenity', metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True,
                                nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True,
                                nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="delete",
                               backref="place")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """retrieves all reviews given place"""
            from models import storage
            reviews_dict = storage.all(Review)
            reviews_list = []
            for values in reviews_dict.values():
                if values.place_id == self.id:
                    reviews_list.append(values)
            return reviews_list

        @property
        def amenities(self):
            "getter for amenities"
            from models import storage
            amenity_dict = storage.all(Amenity)
            amenity_list = []
            for values in amenity_dict.values():
                if values.id in amenity_ids:
                    amenity_list.append(values)

        @amenities.setter
        def amenities(self, obj):
            if obj.__name__ == 'Amenity':
                amenity_ids.append(obj.id)
            else:
                return
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
