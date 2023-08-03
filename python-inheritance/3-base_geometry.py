"""BaseGeometry module with an empty class"""
class BaseGeometry():
        """ an empty class BaseGeometry"""

        def __dir__(cls) -> None:
                
                """get rid of all attributes for this class and exclude __init__subclass"""

                attributes = super().__dir__()
                J_attributes = []
                for attr in attributes:
                        if attr != "__init_Subclass__":
                                J_attributes.append(attr)
                                pass   
                return J_attributes
                                

               

        
        