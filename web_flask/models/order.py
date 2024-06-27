#!/usr/bin/python3
"""This is the order class"""

from app import db

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Table, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



class OrderProduct(Base):
    __tablename__ = 'order_product'

    order_id = db.Column(db.String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.String(60), ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)


class Order(Base):
    """Representation of Order"""
    __tablename__ = 'orders'

    id = db.Column(db.String(60), primary_key=True)
    user_id = db.Column(db.String(60), ForeignKey('users.id'), nullable=False)
    market_name = db.Column(db.String(128), nullable=False)

    products = relationship("Product", secondary='order_product', back_populates="orders")

    def __init__(self, *args, **kwargs):
        """Initializes Order"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        
        @property
        def products(self):
            """Getter attribute returns the list of Product instances"""
            from models.product import Product
            product_list = []
            all_products = models.storage.all(Product)
            for product in all_products.values():
                if product.order_id == self.id:
                    product_list.append(product)
            return product_list