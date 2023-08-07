#!/usr/bin/python3
"""The mmodels base file"""

class Base:
    """The Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """The class Constructor Method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 