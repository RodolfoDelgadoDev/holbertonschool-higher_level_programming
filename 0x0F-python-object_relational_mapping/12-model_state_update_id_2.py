#!/usr/bin/python3
'''script that changes the name of a State object
from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''Create a conection'''
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Makes a session'''
    Session = sessionmaker(engine)
    session = Session()
    '''updating state'''
    s = session.query(State).filter(State.id == 2).first()
    s.name = "New Mexico"
    session.add(s)
    session.commit()
    session.close()
