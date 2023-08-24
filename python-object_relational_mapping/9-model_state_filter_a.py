#!/usr/bin/python3
"""A lists of states obtained containing
the letter a from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            """Usage: {} <mysql username>
            <mysql password> <database name>""".format(sys.argv[0]))
        sys.exit(1)

    mouse = sys.argv[1]
    password = sys.argv[2]
    hbtn_0e_6_usa = sys.argv[3]

    """Establish the engine session"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mouse, password, hbtn_0e_6_usa),
        pool_pre_ping=True
    )


    Session = sessionmaker(bind=engine)
    session = Session()

    """Print a lists state Obtained containing the letter a with queries"""
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    """close the session"""
    session.close()
