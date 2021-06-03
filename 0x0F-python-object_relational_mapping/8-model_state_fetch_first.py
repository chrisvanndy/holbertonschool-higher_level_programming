#!/usr/bin/python3
""" Create an engine"""

from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create the engine connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3],
                                   pool_pre_ping=True))

    # engine inherits Base class attributes
    Base.metadata.create_all(engine)

    # use session maker to bind session to engine connection
    Session = sessionmaker(bind=engine)

    # create instance of Session
    sesh = Session()

    # query State class which contains state table, return the first() object
    state = sesh.query(State).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
