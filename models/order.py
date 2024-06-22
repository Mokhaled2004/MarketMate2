#!/usr/bin/python3
"""Defines the Order class."""

import shlex
from sqlalchemy.ext.declarative import declarative_base
from Models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from Models.product import Product

order_product = Table ("order_product", Base.metadata,
                      Column("order_id", Integer, ForeignKey("orders.order_id"), primary_key=True),
                      Column("product_id", Integer, ForeignKey("products.product_id"), primary_key=True))


class Order(BaseModel, Base):
    
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    market_name = Column(String(128), nullable=False)
    user = relationship("User", back_populates="orders")
    price = Column(Integer, nullable=False)
   
    
    if getenv("MarketMate_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="user")

        product = relationship("product", secondary= order_product,
                                 viewonly=False,
                                 back_populates="order_product")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = Models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.user_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def products(self):
            """ Returns list of amenity ids """
            return self.product_ids

        @products.setter
        def products(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Models.product and obj.id not in self.product_ids:
                self.product_ids.append(obj.id)
    

        
