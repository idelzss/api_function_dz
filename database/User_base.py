from .base import BASE
from sqlalchemy import Column, String, Integer



class User(BASE):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    age = Column(Integer)






