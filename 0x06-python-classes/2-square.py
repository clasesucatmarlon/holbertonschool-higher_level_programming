#!/usr/bin/python3
"2-square.py define"


class Square:
    """ class Square
    """

    def __init__(self, size=0):
        """Inizialitation of variables
        Arg self identificador
        size tamañe of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
