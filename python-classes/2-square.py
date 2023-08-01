"""This represents class of Square that
   defines the Area of a square"""
class Square:
    """This represent Area of a square"""
    def __init__(self, size=0):
        """Size here is a private instance attribute"""
        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the current square area for
        Public instance method"""
        return self.__size ** 2