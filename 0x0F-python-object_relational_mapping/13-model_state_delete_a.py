#!/usr/bin/python3
"""
script that deleted for a name state to database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        user, passwd, host, port, database), pool_pre_ping=True)
    """ Base.metadata.create_all(engine) """
    Session = sessionmaker(bind=engine)
    session = Session()

    filter = session.query(State).filter(State.name.contains("a"))
    for data in filter:
        session.delete(data)
    session.commit()
    session.close()
