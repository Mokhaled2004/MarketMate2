#!/usr/bin/python3
"""create a unique FileStorage instance for yourr application"""
from os import getenv



storage_t = getenv("MarketMate_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
