"""This is a Full Rectangle 
   that inherit from BaseGeometry
"""


class AMetaClass(type):
        """ A Meta class with all the attributes"""

        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in 
                    super().__dir__() if attribute != '__init_subclass__']
        

class BaseGeometry(metaclass=AMetaClass):
        """ an empty class BaseGeometry"""

        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super.__().__dir__() if attribute != '__init_subclass__']
     
      
class BaseGeometry(metaclass=AMetaClass):

    """Public instance method that
       raise an Exception"""

    def area(self):
        """Raise an exception that 
           area is not implemented"""
        raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
         """This is an integer validator 
            that assign value"""
        if not isinstance(value, int):
         raise TypeError("{} must be an integer".format(name))
        if value <= 0:
         raise ValueError("{} must be greater than 0".format(name))
 
    
    def __dir__(cls) -> None:
                """Removing __init_subclass"""

                attributes = super().__dir__()

                return [attribute for attribute in 
                    super().__dir__() if attribute != '__init_subclass__']

        
class BaseGeometry(metaclass=AMetaClass):
    """Public instance method that
       raise an Exception"""

    def area(self):
        """Raise an exception that 
           area is not implemented"""
        raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
         """This is an integer validator
            that assign value"""
        if not isinstance(value, int):
         raise TypeError("{} must be an integer".format(name))
        if value <= 0:
         raise ValueError("{} must be greater than 0".format(name))

    def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in 
                    super().__dir__() if attribute != '__init_subclass__']
    
BaseGeometry = __import__('5-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
      """A subclass"""
      def __init__(self, width, height):
                """The width and height integers
                   of the rectangle"""
                self.__width = 0
                self.__height = 0
                self.integer_validator("width", width)
                self.integer_validator("height", height)
                self.__width = width
                self.__height = height

      def integer_validator(self, name, value):
            """This is an integer validator that assign value"""
            if not isinstance(value, int):
             raise TypeError("{} must be an integer".format(name))
            if value <= 0:
             raise ValueError("{} must be greater than 0".format(name))
            
Rectangle = __import__('6-rectangle').Rectangle

class Rectangle(BaseGeometry):
     """A Full rectangle that 
        inherit from BaseGeometry"""
     def __init__(self, width, height):
          """The width and height 
             integers of the rectangle"""
          self.__width = 0
          self.__height = 0
          self.integer_validator("width", width)
          self.integer_validator("height", height)
          self.__width = width
          self.__height = height


     def area(self):
          """The area must be implemented"""
          return self.__width * self.__height
     
     def __str__(self):
          """Return the Rectangle string"""
          return f"[Rectangle] {self.__width}/{self.__height}"
     
     def area(self):
          """The area must be implemented"""
          return self.__size ** 2 
     
     def __str__(self):
          """Return the Rectangle string"""
          return f"[Rectangle] {self.__size}/{self.__size}"

     
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
     """The square of the Rectangle"""

     def __init__(self, size):
          """The width and height 
             integers of the rectangle"""
          self.__size = size
          self.integer_validator("size", size)

        
     def area(self):
          """The area must be implemented"""
          return self.__size ** 2 
     
     def __str__(self):
          """Return the Rectangle string"""
          return f"[Rectangle] {self.__size}/{self.__size}"
