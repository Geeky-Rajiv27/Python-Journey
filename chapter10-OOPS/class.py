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
    
    def methodName(self,paramter):          #NOTE:---> This is method/member functions of the class Employee
        print(f"Hello employee {self.name}")

    def __init__(self,name,class):          #NOTE:---> This is constructor  of the class.We cannot customize the name
        self.name = "ram"                       of the constructor since it is fixed and doesn't support constructor
        self.class = 10                             overloading.

    def __del__(self):                       #NOTE:---> This is destructor. This is also fixed and we cannot change the     
       print(f"Destructor is called for {self.name}")        name We get to use destructor very less(rarely) since python uses
                                                     automatic garbage collection.

                                                     
NOTE:#creating object / Instantiation -----> This is for normal class attributes

Rajiv = Employee()      ---> Rajiv is an object for class Employee
print(f"The salary of Rajiv is {Rajiv.salary}")


NOTE:#creating object / Instantiation -----> This is for constructor

emp1 = Employee("Aman", 9)  --->NOTE: "Aman" and 9 are instance attributes
print(emp1.name, emp1.class)

NOTE:#way to delete destructor:
emp1 del        --> Deleting object(emp1) which is controlling the constructor and destructor


'''





'''
---------------------------------------------------------------------------------------------------------------
                    Ways to call and set the CONSTRUCTOR
---------------------------------------------------------------------------------------------------------------
'''

class Student:
    def __init__(self,name,semester):
        self.name = name 
        self.semester = semester

    def getData(self):
        print(f"The name of the student is {self.name}")
        print(f"The semester of the student is {self.semester}")


obj = Student("Rajiv", "Third")
obj.getData()


'''
---------------------------------------------------------------------------------------------
    NOTE: Constructor and destructor of python are callled[dunder methods]
    --> This are the methods which are automatically created whenever a new object is created
    --> Basically, [Dunder methods] starts and ends with double underscores (__init__)/(__del__)
---------------------------------------------------------------------------------------------
'''


'''
---------------------------------------------------------------------------------------------
            Important notes about Destructor triggring
---------------------------------------------------------------------------------------------
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' created")

    def __del__(self):
        print(f"Destructor called for '{self.name}'")

# Create an object
obj1 = MyClass("Object 1")
obj2 = obj1  #NOTE: A second reference to the same object

#NOTE: Deleting obj1 does not call the destructor because obj2 still references it
del obj1

#NOTE: Deleting the last reference calls the destructor
del obj2
------------------------------------------------------------------------------------------
'''

'''
---------------------------------------------------------------------------------------------
           STATIC METHODS IN PYTHON :
---------------------------------------------------------------------------------------------

NOTE: like sometime we use a function/methods where there is no any object attributes like nothing 
         and if we are just printing some messages via that methods then we can avoid using (self.)
         But to do so we need to mark the particular method a (static methods)

    SYNTAX:

        @staticmethod
        def method_Name():
            priint("Only messages no object attributes !")

'''

