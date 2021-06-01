#!/usr/bin/python3
""" Create an engine"""

from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3],
                                   pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    sesh = Session()

    state = sesh.query(State)

    for st in state:
        if 'a' in st.name:
            print("{}: {}".format(st.id, st.name))
