#!/usr/bin/python3
#!/usr/bin/python3
"""class Rectangle that defines a rectangle
    """


class Rectangle:
    """class rectangle
    """

    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[summary]

        Arguments:
            value {[type]} -- [description]

        Raises:
            TypeError: [width must be an integer]
            TypeError: [width must be >= 0]
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Arguments:
            value {[type]} -- [description]

        Raises:
            TypeError: [height must be an integer]
            TypeError: [height must be >= 0]
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """[summary]

        Returns:
            [type] -- [area]
        """
        return self.width * self.height

    def perimeter(self):
        """[summary]

        Returns:
            [type] -- [perimeter]
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """[summary]

        Returns:
            [type] -- [rectangle]
        """
        if self.width == 0 or self.height == 0:
            return ""
        size = "#" * self.width

        return (size + "\n") * self.height

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
