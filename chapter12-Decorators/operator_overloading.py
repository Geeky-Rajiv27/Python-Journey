
'''

🔹 What is __str__ in Python?

__str__ is a special (dunder) method used to define a human-readable string representation of an 
    object.

It’s what gets called when you do:

print(obj)
str(obj)
If you don’t define __str__, Python falls back to the default implementation from object, which looks like:

<__main__.ClassName object at 0x...>

(that memory address style output you’ve seen before).
--------------------------------------------------------------------------------------------------------

🔹 Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    

p1 = Person("Rajiv", 21)
print(p1)         # calls __str__ automatically
print(str(p1))    # also calls __str__


Output:

Rajiv, 21 years old
Rajiv, 21 years old
--------------------------------------------------------------------------------------------------------
🔹 Difference between __str__ and __repr__

__str__ → for human-readable output (friendly, clear for end users).

__repr__ → for developer/debug output (unambiguous, should help recreate the object).

Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Rajiv", 21)
print(str(p))   # Rajiv, 21 years old
print(repr(p))  # Person('Rajiv', 21)
--------------------------------------------------------------------------------------------------------

🔹 Why is __str__ useful?

Makes print(obj) give meaningful info.

Helps debugging / logging.

Often used together with operator overloading to give nice display of custom objects (e.g., Complex numbers, Vectors, etc.).

👉 So, __str__ is not about operator overloading itself, but it is often implemented alongside operator overloading so your custom objects look nice when printed.
--------------------------------------------------------------------------------------------------------

'''

'''
Q1. Complex Numbers

Create a Complex class that supports:

Addition (+)

Multiplication (*)

Equality check (==)

A nice string representation (__str__ or __repr__)
'''



class Complex:
    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag
    
    def __str__(self):
        return f"{self.real}+{self.imag}i"  # this is responsible for displaying output (nice string representation only)
    
    def __add__(self, c2):  # Here we define the meaning of the overloaded (symbol) for eg: in this case we have(+)
        return Complex(self.real + c2.real, self.imag + c2.imag)
    
    #making another dunder method for next type of string representation (for complex multiplication)
#-----> actually we don't need to make such thing since the output of complex multiplication also same as addtion
    #   but we have to use dunder method __mul__ where we will explain the meaning of (*) this symbol

    def __mul__(self, c2):  #--- here we can also replce c2 with(other)
    #we. cannot do in such a way since Complex() accepts 2 arguments but here we are trying to pass a single at once
        # return Complex((self.real * c2.real - self.imag * c2.imag) + (self.real * c2.imag + self.imag * c2.real))
        real_part = (self.real * c2.real - self.imag * c2.imag)
        imag_part = (self.real * c2.imag + self.imag * c2.real)
        return Complex(real_part, imag_part)


    #defining function of (==) symbol 
    def __eq__(self, c2):
        if(self.real == c2.real and self.imag == c2.imag):
            return "Yes, both complex numbers are same"

        else:
            return "No, both complex numbers are not same"
            
        
        
c1 = Complex(1,2)
c2 = Complex(1,2)


# print(str(c1 + c2))# This format of calling the dunder method __str___ can also be used
print(f"The addition of two complex number : {c1+c2}")    # this can also be used
print(f"The multiplication of two complex number : {c1 * c2}")
print(c1 == c2)

    

'''--------------------------------------------------------------------------------------------------------
    Write a class vector representing a vector of n dimensions. Overload the (+) and (*) operator
    which calculates the sum and dot(.) product of them.
--------------------------------------------------------------------------------------------------------
'''

class Vector:
    def __init__(self, i, j):
        self.i = i 
        self.j = j
    
    def __str__(self):
        return f"{self.i}+{self.j}"
    
    def __add__(self, v2):
        return f"{self.i + v2.i}i + {self.j + v2.j}j"
    
    def __mul__(self, v2):
        return self.i * v2.i + self.j * v2.j
        
v1 = Vector(1,2)
v2 = Vector(1,2)

print(f"The addition of two vectors are : {v1+v2}")
print(f"The dot product of two vectors : {v1 * v2}")