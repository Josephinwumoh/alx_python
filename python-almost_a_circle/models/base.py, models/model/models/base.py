# models/base.py
"""The base file module"""
class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The Constructor Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

