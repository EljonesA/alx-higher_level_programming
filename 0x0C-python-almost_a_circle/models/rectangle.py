#!/usr/bin/python3
""" Module with class that inherits from Base class """

from models.base import Base


class Rectangle(Base):
    """
    Child class of Base class

    Attributes:
        __width:
        __heigth
        __x
        __y
        id

    Methods:
        __init__: class constructor
        area: computes area of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle class constructor

        Args:
            width
            height
            x
            y
            id
        """
        super().__init__(id)  # call constructor of base class

        # validate width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        # validate height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        # validate x
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        #  validate y
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        Args:
            width: new width value
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height getter
        Args:
            height: new height value
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        Args:
            x: new x value
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y setter
        Args:
            y: new y value
        """
        if not isinstance(y, int):
            raise ValueError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Method that computes area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Method that draws the rectanngle using '#' char """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ str representation of the Rectangle class """
        return (f"[Rectangle]({self.id}) {self.__x}/{self.__y}"
                "- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ method that updates class attributes using CL arguments """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dict representation of a REctangle """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
