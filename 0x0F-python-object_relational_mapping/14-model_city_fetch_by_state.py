#!/usr/bin/python3
"""
script that deleted for a name state to database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City

if __name__ == "__main__":
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        user, passwd, host, port, database))
    """ Base.metadata.create_all(engine) """
    Session = sessionmaker(bind=engine)
    session = Session()

    To_query = session.query(City).join(State).order_by(City.id).all()
    for data in To_query:
        print("{}: ({}) {}".format(data.state.name, data.id, data.name))
    session.close()
