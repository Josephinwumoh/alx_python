"""An integer validator"""

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
        
class BaseGeometry(metaclass=AMetaClass):

    """This shows public instance Method"""

    def area(self):
        """Raise an exception that area is not implemented"""
        raise Exception("area() is not implemented")
    
           
    def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
        
class BaseGeometry(metaclass=AMetaClass):
    """Public instance method that raise an Exception"""
    
    def integer_validator(self, name, value):
        """This is an integer validator that assign value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
    def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']