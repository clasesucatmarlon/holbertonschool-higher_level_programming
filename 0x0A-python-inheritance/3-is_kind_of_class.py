#!/usr/bin/python3
"""function that returns True if the object is an instance
    """


def is_kind_of_class(obj, a_class):
    """Determine if is instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
