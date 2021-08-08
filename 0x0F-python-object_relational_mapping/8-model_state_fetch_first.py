#!/usr/bin/python3
'''script that prints the first State object from the db hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

'''Create a conection'''
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Makes a session'''
    Session = sessionmaker(engine)
    session = Session()
    '''take the first value'''
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
