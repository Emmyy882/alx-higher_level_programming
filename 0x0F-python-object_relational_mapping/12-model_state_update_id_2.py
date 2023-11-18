#!/usr/bin/python3
"""changes the name of a State objects from the database hbtn_0e_0_usa"""
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

        # Updating the name of State object
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = 'New Mexico'
            session.commit()
