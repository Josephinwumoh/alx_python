"""To access and update private attribute"""
class Square:
    """This represent area of a square"""
    def __init__(self, size=0):
        """Size here is private instance attribute"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This return the current square area for public instance method"""
        return self.__size ** 2
