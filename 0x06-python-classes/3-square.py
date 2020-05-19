#!/usr/bin/python3
"3-square.py define"


class Square:
    def __init__(self, size=0):
        """Inizialitation of variables
        Arg self identificador
        size tamañe of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise value("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size ** 2
