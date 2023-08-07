"""The file Rectangle inherit from Base"""

from models.base import Base

class Rectangle(Base):
    """The Class Rectangle inherits from parent Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """The return attributes width with getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """The private instance attributes width with setter method"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The return attributes height with getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """The private instance attributes height with setter method"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The return attributes x with getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """The private instance attributes x with setter method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The return attributes y with getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """The private instance attributes y with setter method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area must be implemented"""
        return self.__width * self.__height
    
    def display(self):
        """Display the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print('' * self.__x + '#' * self.__width)

    def display(self):
        """Display the character #"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """Return the Rectangle string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def display(self):
        """Display the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( ' ' *  self.__x  +  '#'  *  self.__width)