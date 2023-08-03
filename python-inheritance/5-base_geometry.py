"""An integer validator"""

class BaseGeometry:
    """Public instance method that raise an Exception"""

    def Area(self):
        """This raise an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """This is an integer validator that assign value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))