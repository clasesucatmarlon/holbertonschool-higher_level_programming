#!/usr/bin/python3
"""My integer
    """


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __init__(self, value):
        self.__value = value

    def __eq__(self, tmp):
        return self.__value != tmp

    def __ne__(self, tmp):
        return self.__value == tmp
