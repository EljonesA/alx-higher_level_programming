#!/usr/bin/python3
""" Module with child class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Child class of Rectangle class

    Attributes:
        all parent class attributes >> height = width = size

    Methods:
        __init__: class constructor >> superclass constructor
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        Args:
            size: of the square
            x
            y
            id (optional)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """
        Size setter
        Args:
            size: new size value
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates class attributes based on command line arguments """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ string representation of Square class """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """ returns dict representation of a Square class """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
