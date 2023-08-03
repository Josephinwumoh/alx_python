"""BaseGeometry module with an empty class"""
from collections.abc import Iterable


class BaseGeometry():
        """ an empty class BaseGeometry"""
        pass

class dir(BaseGeometry):
        """Here is the override"""

        def __dir__(self) -> Iterable[str]:
                return super().__dir__()

    
                                

               

        
        