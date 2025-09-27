'''
NOTE: Abstract base classes are the type of of class in python which are derived from (ABC) this classes contains
    various (abstract methods).

    Abstract method : abstract method are the type of method which do not have any implementation of body

    --> we cannot create object of abstract classes.

    NOTE: The class that is inherited from abstract base classes must inherit the abstract method otherwise 
        we cannot create objects of those child classes
    
    NOTE:we need to import (ABC), abstract methods form abc module

    NOTE: abstract class is just a blueprint of the sub-classes
'''


'''
----------------------------------------------------------------------------------------------------
                SYNTAX OF ABSTRACT CLASSES :
----------------------------------------------------------------------------------------------------
'''
from abc import ABC, abstractmethod

#abstract classes
class shape(ABC):   #this is derived from ABC so called abstract classes


    @abstractmethod
    def area(self): # here is no body implementation
        pass

class rectangle(shape):
    def __init__(self, l, b):
        self.l = l 
        self.b = b

    def area(self):
        return self.l * self.b
    
class square(shape):
    def __init__(self, l, b):
        self.l = l 
        


    def area(self):
        return self.l * self.l
    
r = rectangle(2,3)
print(f"The area of rectangle is : {r.area()}")

s = square(2,2)
print(f"The area of square is : {s.area()}")