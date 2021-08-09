#!/usr/bin/python3
'''script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa'''
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
    '''adding state'''
    st = State(name='Louisiana')
    session.add(st)
    session.commit()
    s = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(s.id))
    session.close()
