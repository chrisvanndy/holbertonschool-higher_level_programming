#!/usr/bin/python3
""" Creates an engine to query multiple tables"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
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

    for c, s in sesh.query(City, State).filter(City.state_id == State.id).all():
        print("{} ({}) {}".format(s.name, s.id, c.name))

