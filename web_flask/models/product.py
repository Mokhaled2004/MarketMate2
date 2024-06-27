#!/usr/bin/python3
"""This is the product class"""
from app import db
from sqlalchemy import Column, Integer, String, Float
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Table
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):

    """Representation of Product"""
    

    __tablename__ = 'products'
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(128), nullable=False)
    orders = db.relationship("Order", secondary='order_product', back_populates="products")


        
   

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)
