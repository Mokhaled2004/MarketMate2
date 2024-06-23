#!/usr/bin/python3
"""This is the product class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float, Table

class Product(BaseModel, Base):
    """Representation of Product"""
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    orders = relationship("Order", secondary="order_product", back_populates="products")

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)
