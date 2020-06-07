#!/bin/usr/python3
"""test rectangle
    """

import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8

class TestRectangle(unittest.TestCase):
    """ test
    """
    def test_docstring(self):
        """test Docstrings
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__width.__doc__)
        self.assertIsNotNone(height.__doc__)
        self.assertIsNotNone(x.__doc__)
        self.assertIsNotNone(y.__doc__)
        self.assertIsNotNone(area.__doc__)
        self.assertIsNotNone(display.__doc__)
        self.assertIsNotNone(__str__.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

