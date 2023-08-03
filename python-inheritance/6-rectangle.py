"""This is a rectangle that inherit from BaseGeometry
"""

class AMetaClass(type):
        """ A Meta class with all the attributes"""

        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=AMetaClass):
        """ an empty class BaseGeometry"""

        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class Rectangle(BaseGeometry):
        """A rectangle with width and height"""

        def __init__(self, width, height):
                """The width and height integers of the rectangle"""
                self.integer_validator = ("width", width)
                self.integer_validator = ("height", height)
                self.width = width
                self.height = height
                
        def __str__(self):
                "Return the string of the Rectangle"
                return ("[Rectangle] {}/{}".format(self.width, self.height))
        
        def area(self):
                """Calculate the area of the rectangle"""
                return self.width * self.height
        
        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

                
        