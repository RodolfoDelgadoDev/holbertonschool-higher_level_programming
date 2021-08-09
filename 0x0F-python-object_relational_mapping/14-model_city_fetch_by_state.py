#!/usr/bin/python3
'''script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from model_city import City
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
    '''Print cities'''
    c = session.query(City, State).join(State).order_by(City.id)
    for raw in c:
        print("{}: ({}) {}".format(raw[1].name, raw[0].id, raw[0].name))
    session.close()
