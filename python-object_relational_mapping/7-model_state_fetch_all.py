#!/usr/bin/python3
"""All States via SQLALchemy"""

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

    """Establish the engine and session"""
    engine = create_engine(
                        """mysql+mysqldb://{}:{}
                        @localhost/{}""".format(
                        mouse, password, hbtn_0e_6_usa),
                        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Print all state Objects including there queries"""
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    """Close session"""
    session.close()
