"""A function that return True if the is an instance
of the class that inherit directly or indirectly"""


def inherits_from(obj, a_class):

    """This is subclass of a class that inherits
    directly or indirectly"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
