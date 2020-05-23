#!/usr/bin/python3
"""
Unittest determinate max value integer of list

"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestUnitary(unittest.TestCase):
    """
    Test max integer to list

    """

    def test_max_in_the_middle(self):
        """tests standard operation"""
        test_list = [1, 2, 99, 3, 4]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_at_the_end(self):
        """standard operation: max is at the end"""
        test_list = [1, 2, 3, 4, 99]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_at_the_beginning(self):
        """standard operation: max is at the beginning"""
        test_list = [99, 1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_one_negative(self):
        """standard operation: list containing one negative value"""
        test_list = [-99, 1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_all_negative(self):
        """standard operation: list containing all negative values"""
        test_list = [-99, -1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)

    def test_max_one_element(self):
        """standard operation: list containing only one element"""
        test_list = [99]
        self.assertEqual(max_integer(test_list), 99)

    def test_arg_empty_list(self):
        """tests empty list argument"""
        self.assertIs(max_integer([]), None)

    def test_arg_noargs(self):
        """test no arguments"""
        self.assertIs(max_integer(), None)
