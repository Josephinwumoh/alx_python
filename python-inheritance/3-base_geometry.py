"""BaseGeometry module with an empty class"""
class BaseGeometry:
        """ an empty class BaseGeometry"""

        def __dir__(cls) -> None:
                
                """get rid of all attributes for this class and exclude __init__subclass"""

                attributes = super().__dir__()
                list_to_return = []
                for attr in attributes:
                        if attr != "__init__Subclass":
                                #append this to the list_to_return
                                pass
                        return list_to_return
                                

               

        
        