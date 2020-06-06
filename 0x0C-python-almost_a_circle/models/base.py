#!/usr/bin/python3
"""module base
    """


class Base:
    """Base class with methods
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
