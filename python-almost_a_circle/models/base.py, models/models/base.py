#!/usr/bin/python3
"""The models base file module"""

class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

