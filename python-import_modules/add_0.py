#! /usr/bin/python3
def add(a, b):

  """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    
    
    
    """
  return a + b 

def FAKE(a, b):
   

  return  a - b
  
print(__name__)
print(FAKE(1, 2))
print(FAKE(10, 30))
print(FAKE(-10, 30))
print(FAKE(-10, -30))