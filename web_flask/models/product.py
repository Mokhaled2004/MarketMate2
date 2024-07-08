#!/usr/bin/python3
"""This is the product class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):

    """Representation of Product"""
    if models.storage_t == 'db':

        __tablename__ = 'products'
        name = Column(String(128), nullable=False)
        price = Column(Float, nullable=False)
        orders = relationship("Order", secondary='order_product', back_populates="products")


    else:
        
        user_id = ""
        titlee = ""
        price = 0.0
        quantity = 0
        image = ""

    def __init__(self, *args, **kwargs):

               super().__init__(*args, **kwargs)
