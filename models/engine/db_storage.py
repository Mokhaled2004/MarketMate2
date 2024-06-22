#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.order import Order
from models.review import Review
from models.product import Product
from os import getenv

classes = {"Order": Order, "Product": Product,
           "User": User, "Review": Review}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None
    

def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv('MarketMate_MYSQL_USER')
        passwd = getenv('MarketMate_MYSQL_PWD')
        host = getenv('MarketMate_MYSQL_HOST')
        db = getenv('MarketMate_MYSQL_DB')
        env = getenv('MarketMate_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
                                            
                                        
        if env == "test":
                Base.metadata.drop_all(self.__engine)
            
def all(self, cls=None):
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [Product,Order, User, Review]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
    
    
def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        
def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if obj is not None:
        self.__session.delete(obj)  
        
def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
        
        
def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
        
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
             
        