#!/usr/bin/python3
'''file that contains the class definition
City and an instance base = declarative_base()'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
'''City Class'''


class City(Base):
    '''City'''

    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey(State.id), nullable=False)
