#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_0_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 4:

        # connecting to MySQL server
        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                pool_pre_ping=True
                )

        # Create all tables in the database
        Base.metadata.create_all(engine)

        # creating a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Printing the first object
        result = session.query(State).first()
        if result is not None:
            print('{}: {}'.format(result.id, result.name))
        else:
            print("Nothing")
