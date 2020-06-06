#!/usr/bin/python3
"""square base
    """


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    clas Rectangle witch inheriys from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        task 10 - width = height = size
        initiatize the squard object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        task 10
        print representation rectangle instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter for size attribute
        """
        self.width = value
        self.height = value
