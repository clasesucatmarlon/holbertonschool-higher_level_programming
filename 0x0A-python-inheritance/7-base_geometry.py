#!/usr/bin/python3
"""class BaseGeometry (based on 5-base_geometry.py)
    """


class BaseGeometry:
    """contains area only
    """

    def area(self):
        """nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate values
        """
        if type(value) in not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
