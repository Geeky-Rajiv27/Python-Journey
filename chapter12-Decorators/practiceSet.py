'''-----------------------------------------------------------------------------------------------------
    1) Create a class (2-D vector) and use it to create another class representing a 3-D vector
-----------------------------------------------------------------------------------------------------

class Two_D_Vector:
    def __init__(self, i , j):
        self.i = i 
        self.j = j

    def show(self):
        print(f"The 2D vectors are : {self.i}i + {self.j}j")

class Three_D_Vector(Two_D_Vector):
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.k = k 
    def show(self):
        print(f"The 2D vectors are : {self.i}i + {self.j}j + {self.k}k")

dimension_2 = Two_D_Vector(1, 2)
dimension_3 = Three_D_Vector(1, 2, 3)

#now printing
dimension_2.show()
dimension_3.show()
'''

        
'''-----------------------------------------------------------------------------------------------------
    2)Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'.
     Add a method 'bark' to class 'Dog'
-----------------------------------------------------------------------------------------------------

class Animals:
    def sound(self):
        print("This is animal sound")

class Pets(Animals):
    def sound(self):
        print("This is Pets sound")

class Dog(Pets):
    def brak(self):
        print("Dog : bhau bhau")

d = Dog()
d.brak()

'''


'''-----------------------------------------------------------------------------------------------------
    3) Create a class 'Employee' and add salary and increment properties to it.

        write a method 'salaryAfterIncrement' method with a @property decorator with a setter
        which changes the value of increment based on the salary
-----------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.__increment = increment

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.__increment)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, amount):
        if(amount > 0):
            self.__increment = amount
        else:
            print("Increment must be greater than 0 \n")

emp = Employee(124000, 27000)
print(f"The salary after increment is : {emp.salaryAfterIncrement} $")


#setting increment amount using (setter)
emp.salaryAfterIncrement = 76000
print(f"The salary after increment is : {emp.salaryAfterIncrement} $")

'''


'''-----------------------------------------------------------------------------------------------------
    4) Write a class 'Complex' to reperesent complex numbers, along with overloaded opearators '+' 
    and '*' which adds and multiplies them. 

formula for multiplication :(a+bi)(c+di)=(ac-bd)+(ad+bc)i
-----------------------------------------------------------------------------------------------------
'''


class Complex:
    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag

    def complexaddition(self, c2):      # overloading operator c2
        return f"The sum of two complex no : {self.real + c2.real}+{self.imag + c2.imag}i"
    
    def complexMultiplication(self, c2):
        real_part = self.real * c2.real - self.imag * c2.imag
        imag_part = self.real * c2.imag + self.imag * c2.real

        return f"Multiplication of two no : {real_part}+{imag_part}"
        

#complex addition
c1 = Complex(1,2)
c2 = Complex(1,2)


print(c1.complexaddition(c2))

#complex multiplication 
c1 = Complex(1,2)
c2 = Complex(1,2)

print(c1.complexMultiplication(c2))
