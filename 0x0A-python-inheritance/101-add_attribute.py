#!/usr/bin/python3
"""adds an attribute
    """


def add_attribute(obj, name, value):
    """adds attributes
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
