#!/bin/usr/python3
"""test base
    """

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test base
    """

    def test_instance(self):
        var1 = Base()
        var2 = Base(9)
        var3 = Base(11.5)
        var4 = Base(None)
        var5 = Base("string")
        var6 = Base({})
        var7 = Base(())
        var8 = Base([])

        self.assertEqual(var1.id, 1)
        self.assertEqual(var2.id, 9)
        self.assertEqual(var3.id, 11.5)
        self.assertEqual(var4.id, 2)
        self.assertEqual(var5.id, 'string')
        self.assertEqual(var6.id, {})
        self.assertEqual(var7.id, ())
        self.assertEqual(var8.id, [])

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/rectangle.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")