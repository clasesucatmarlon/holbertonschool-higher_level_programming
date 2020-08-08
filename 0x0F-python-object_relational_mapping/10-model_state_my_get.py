#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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
    name_input = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        user, passwd, host, port, database), pool_pre_ping=True)
    """ Base.metadata.create_all(engine) """
    Session = sessionmaker(bind=engine)
    session = Session()

    filter_value = session.query(State).filter_by(name=name_input).first()
    if filter_value:
        print("{}".format(filter_value.id))
    else:
        print("Not found")
    session.close()
