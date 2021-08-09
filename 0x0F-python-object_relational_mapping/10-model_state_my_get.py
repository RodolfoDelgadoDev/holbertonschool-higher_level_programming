#!/usr/bin/python3
'''script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa'''
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
    '''Loop to print all the table'''
    s = session.query(State).filter(State.name == sys.argv[4]).first()
    if s:
        print("{}".format(s.id))
    else:
        print("Not found")
    session.close()
