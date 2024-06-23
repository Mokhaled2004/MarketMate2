#!/usr/bin/python3
"""This is the order class"""
import shlex
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models

order_product = Table('order_product', Base.metadata,
                      Column('order_id', String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                      Column('product_id', String(60), ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

class Order(BaseModel, Base):
    """Representation of Order"""
    __tablename__ = 'orders'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    market_name = Column(String(128), nullable=False)
    products = relationship("Product", secondary=order_product, back_populates="orders")

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)
