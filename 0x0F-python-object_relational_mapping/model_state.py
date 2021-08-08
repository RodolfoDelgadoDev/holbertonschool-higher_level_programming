#!/usr/bin/python3
'''file that contains the class definition 
State and an instance base = declarative_base()'''
from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
'''State Class'''
class State(Base):
    '''State'''
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
