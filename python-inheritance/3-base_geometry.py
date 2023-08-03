"""BaseGeometry module with an empty class"""

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
