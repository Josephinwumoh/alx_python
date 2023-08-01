"""To Access an Update Private Attribute"""
class Square:
    """This represents the private instance
      attribute for size"""
    def __init__(self, size=0):
        """This shows the initialization for
        the square is zero"""
        self.size = size
    def size(self):
        """Here is Getter Method to 
        validate the assignment of a private attribute"""
        return self.__size
    def size(self, value):
        """Here is the Setter Method used in 
        defining how getting the attribute value"""
        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        if value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value
    def area(self):
        """Returns the current square area for
        Public instance method"""
        return self.__size ** 2