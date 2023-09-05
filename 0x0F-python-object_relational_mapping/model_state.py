#!/usr/bin/python3
"""Contains definition of class 'State' and an instance
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

"""This is the main body of the script
"""

if __name__ == "__main__":
    """I am just testing documentation here
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
