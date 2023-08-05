"""This is a Full Rectangle that inherit from BaseGeometry"""


Rectangle = __import__('7-rectangle').Rectangle
"""The file Rectangle from 7-rectangle"""
class Square(Rectangle):
    """The square of the Rectangle"""

    def __init__(self, size):
      """The width and height integers of the rectangle"""
      self.__size = size
      self.integer_validator("size", size)

    def area(self):
      """The area must be implemented"""
      return self.__size ** 2 
     
    def __str__(self):
     """Return the Rectangle string"""
     return f"[Rectangle] {self.__size}/{self.__size}"
