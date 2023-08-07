#!/usr/bin/python3
"""The file Square that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """The class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)