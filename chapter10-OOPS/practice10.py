'''
-------------------------------------------------------------------------------------------
    Create a class "Programmer" for storing informaion of programmers working at Microsoft
-------------------------------------------------------------------------------------------
'''

class Programmer:
    def __init__(self ,name, salary, language, Post):
        self.name = name
        self.salary = salary
        self.language = language
        self.Post = Post

    def getData(self):
        print(f"The details of the Programmer are : \n")
        print(f"The name of the Programmer is {self.name}")
        print(f"The salary of the Programmer is {self.salary}")
        print(f"The favourite language of the Programmer is {self.language}")
        print(f"The Post of the Programmer is {self.Post}")
        print("\n")

prog1 = Programmer("Rajiv", 12400 , "Python" , "Senior_AI/ML_Engineer")
prog2 = Programmer("Aman", 10400 , "React" , "junior_React_dev")
prog3 = Programmer("SID", 88000 , "C++" , "System_dev")
prog4 = Programmer("Punam", 50000 , "Python" , "UI/UX_designer")


prog1.getData()
prog2.getData()
prog3.getData()
prog4.getData()




'''
-----------------------------------------------------------------------------------------------------------
        Make a class 'calculator' capable of calculating square root, cube root and square of the numbers
-----------------------------------------------------------------------------------------------------------
NOTE: power raising method :
  1) for square root = print(num ** (1/2))
  2) for cube root = not available

NOTE: pow() method :
    1)for square root = print(pow(num, (1/2)))
    2)for cube root = print(pow(num, (1/3)))

# from math import sqrt  == # if we use this then we have to use in this way : sqqrt(num)
import math # == if we use this then we have to use : math.sqrt(num)

'''

class Calculator:
    def __init__(self, num):
        self.num = num 

    def squareRoot(self):
        sqRoot = math.sqrt(self.num)
        print(f"The square root of the given number is : {sqRoot} \n")

    def cubeRoot(self):
        cbRoot = pow((self.num),(1/3))
        print(f"The cube root of the given number is : {cbRoot} \n")

    def square(self):
        print(f"The square of the given number is : {self.num ** (2)} \n")
        
obj = Calculator(8)
obj.squareRoot()
obj.cubeRoot()
obj.square()




'''
-----------------------------------------------------------------------------------------------------------
        Create a class with a class attribute a; create an object from it and set  'a' directly
        using object.a = 0 . Does this change the class attributes 
                        Ans : No, after setting the instance attribute the value of a remains same.
                            because it will print same value of a i.e ; 1 after using (Attribute.a)  
-----------------------------------------------------------------------------------------------------------
'''

class Attribute:
    a = 1


obj = Attribute()
print("Before setting instance attribute")
print(f"The value of a : {obj.a}") 

obj.a = 2
print("After setting instance attribute")
print(f"The value of a : {obj.a}") 

#checking whether the value of class attributes is changed or not
print(f"The value of class attribute : {Attribute.a}")


'''
-----------------------------------------------------------------------------------------------------------
        Add a static method in problem 2, to greet the user with hello
-----------------------------------------------------------------------------------------------------------
'''

import math
class Calculator:
    def __init__(self, num):
        self.num = num 

    @staticmethod
    def greet():
        print("Hello user\n")

    def squareRoot(self):
        sqRoot = math.sqrt(self.num)
        print(f"The square root of the given number is : {sqRoot} \n")

    def cubeRoot(self):
        cbRoot = pow((self.num),(1/3))
        print(f"The cube root of the given number is : {cbRoot} \n")

    def square(self):
        print(f"The square of the given number is : {self.num ** (2)} \n")
        
obj = Calculator(8)
obj.greet()
obj.squareRoot()
obj.cubeRoot()
obj.square()




'''
-----------------------------------------------------------------------------------------------------------
     Write a class Train which has methods to book a ticket,get status (no of seats) and get fare information
     of train running under Nepal railways
-----------------------------------------------------------------------------------------------------------
'''

class Train:
    
   def bookTicket(self,seatNo):
      self.seatNo = seatNo


   def getStatus(self):
      print("There are total 10 seats available \n")
      print("seat no 1 - 10\n")
      print("Fare for butwal - Palpa : Rs. 200")
      print("Fare for KTM - Pokhara : Rs. 140")
      print("Fare for Butwal to Pokhara: Rs. 90 \n")

   def permission(self):
         print(f"Your seat for  seat no.{self.seatNo} is booked successfully \n")
      
obj = Train()
obj.bookTicket(27)
obj.getStatus()
obj.permission()



