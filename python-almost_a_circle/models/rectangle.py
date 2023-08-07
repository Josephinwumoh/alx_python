#!/usr/bin/python3
"""The file Rectangle inherit from Base"""

from models.base import Base

class Rectangle(Base):
    """The Class Rectangle inherits from parent Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The Class Constructor"""        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """The getter and setter attributes width."""
        return self.__width

    @width.setter
    def width(self, value):
        """The private instance attributes width with setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter and setter attributes height."""
        return self.__height

    @height.setter
    def height(self, value):
        """The private instance attributes height with setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter and setter attributes x."""
        return self.__x

    @x.setter
    def x(self, value):
        """The private instance attributes x with setter method"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter and setter attributes y."""
        return self.__y

    @y.setter
    def y(self, value):
        """The private instance attributes y with setter method"""
        if type(value) != int:
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