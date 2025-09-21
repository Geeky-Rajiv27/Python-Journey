#NOTE: class is a blueprint for creating objects. Objects are also called as instances of classes

'''
---------------------------------------------------------------------------------------------------------------
    CONCEPT OF CLASS IN PYTHON:
---------------------------------------------------------------------------------------------------------------

-----------SYNTAX:-----------

class Employee:
    name = "Rajiv"              ---
    semester = "2nd"            --- This are the class attributes    
    Rollno = 23                 ---
    salary = 13423
    
    def methodName(self,paramter):              ---> This is method/member functions of the class Employee
        print(f"Hello employee {self.name}")

    def __init__(self,name,class):              ---> This is constructor  of the class.We cannot customize the name
        self.name = "ram"                       of the constructor since it is fixed and doesn't support constructor
        self.class = 10                             overloading.

    def __del__(self):                           ---> This is destructor. This is also fixed and we cannot change the     
       print(f"{self.name} is being deleted")        name We get to use destructor very less(rarely) since python uses
                                                     automatic garbage collection.

                                                     
#creating object / Instantiation -----> This is for normal class attributes


Rajiv = Employee()      ---> Rajiv is an object for class Employee
print(f"The salary of Rajiv is {Rajiv.salary}")


#creating object / Instantiation -----> This is for constructor



'''

