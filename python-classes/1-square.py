"""This is a class square that defines a
   square by using task 1(0-square)"""
class Square:
    """This represent class Square"""
    def __init__(self, size=0):
        """size must be an integer otherwise raise a TypeError"""
        if not isinstance(size, int):
            raise TypeError ("size must be an nteger")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size