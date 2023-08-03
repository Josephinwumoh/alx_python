"""BaseGeometry module with an empty class"""

class BaseGeometry():
        """ an empty class BaseGeometry"""

        def __dir__(cls) -> None:
                """getting lists of all attributes for this class and exclude __init_subclass"""
                attributes = super().__dir__()
                b_attributes = []
                for attr in attributes:
                        if attr != '__init_subclass__':
                                b_attributes.append(attr)
                return b_attributes
        
        def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in attributes if attribute != '__init_subclass__']
