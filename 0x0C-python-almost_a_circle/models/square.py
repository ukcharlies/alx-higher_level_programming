#!/usr/bin/python3
"""Module containing Square class
which is a sub class of the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Blueprint of Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of an obect"""

        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """getter method to return
        the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method to set private instance
        variable size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides to return
        "[Square] (<id>) <x>/<y> - <size>"
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args: New attribute values.
                -1st arg represents id attribute
                -2nd arg represents size attribute
                -3rd arg represents x attribute
                -4th arg represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j

        else:
            """if args are not present
            use kwargs to assign attributes"""
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {
            "id" : self.id,
            "size": self.width,
            "x": self.x,
            "y":self.y
        }
