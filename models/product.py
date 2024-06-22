#!/usr/bin/python3
"""Defines the Product  class."""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from models.order import order_product





class Product(BaseModel):
    
    """Represents a product """
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(128), nullable=False)
    stock = Column(Integer, nullable=False)
    order_product = relationship("Order", secondary="order_product")



    
