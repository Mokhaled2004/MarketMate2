#!/usr/bin/python3
""" new class for sqlAlchemy """
import models
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.order import Order
from models.review import Review
from models.product import Product
from models.payment import Payment
from os import getenv
import sqlalchemy

classes = {"Product": Product  , "Review": Review, "Order": Order, "User": User,"Payment": Payment}
class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        MarketMate_MYSQL_USER = getenv("MarketMate_MYSQL_USER")
        MarketMate_MYSQL_PWD = getenv("MarketMate_MYSQL_PWD")
        MarketMate_MYSQL_DB = getenv("MarketMate_MYSQL_DB")
        MarketMate_MYSQL_HOST = getenv("MarketMate_MYSQL_HOST")
        MarketMate_ENV = getenv("MarketMate_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(MarketMate_MYSQL_USER, MarketMate_MYSQL_PWD, MarketMate_MYSQL_HOST, MarketMate_MYSQL_DB),
                                      pool_pre_ping=True)

        if MarketMate_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [ User, Order, Review, Product]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()


    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
