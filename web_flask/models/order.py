#!/usr/bin/python3
"""This is the order class"""


import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Table, String,ForeignKey
from sqlalchemy.orm import relationship



if models.storage_t == 'db':
    order_product = Table('order_product', Base.metadata,
                      Column('order_id', String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                      Column('product_id', String(60), ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))


class Order(BaseModel, Base):
    """Representation of Order"""
    if models.storage_t == 'db':
        _tablename_ = 'orders'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        market_name = Column(String(128), nullable=False)
        address = Column(String(128), nullable=False)
        date = Column(String(128), nullable=False)
        products = relationship("Product", secondary=order_product, back_populates="orders")

    else:

        delivered = "not delivered"
        user_id = ""
        products = []
        total_price = 0.0
        market_name = ""
        address = ""
        date = ""
        

    def _init_(self, *args, **kwargs):
        """initializes Order"""
        super()._init_(*args, **kwargs)

    
        
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
        
        @products.setter
        def products(self, value):
            """Setter attribute sets the list of Product instances"""
            self._products = value
        
   