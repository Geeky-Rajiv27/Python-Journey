'''---------------------------------------------Practice question no - 1----------------------------------
Q1. Basic Family Example

Create three classes:

Grandfather → has an attribute grandfather_name and a method to show it.

Father → inherits from Grandfather, adds father_name.

Son → inherits from Father, adds son_name.

👉 Write a program to display the names of all three generations using a Son object.
'''


class Grandfather:
    def __init__(self, Grandfather_Name):
        self.Grandfather_Name = Grandfather_Name
    
    def showGrandfather_Name(self):
        print(f"The name of the grandfather is : {self.Grandfather_Name}\n")

class Father(Grandfather):
    def __init__(self, Grandfather_Name,father_Name):
        super().__init__(Grandfather_Name)      # calling constructor of grandfather
        self.father_Name = father_Name

    def showfather_Name(self):
        print(f"The name of the father is : {self.father_Name}\n")


class Son(Father):
    def __init__(self, Grandfather_Name,father_Name, son_Name):
     super().__init__(Grandfather_Name, father_Name)        # calling constructor of father
     self.son_Name = son_Name

    def showSon_Name(self):
        print(f"The name of the son is : {self.son_Name}\n")


s = Son("Ram Chaudhary", "Hari Chaudhary", "Shyam Chaudhary")
s.showGrandfather_Name()
s.showfather_Name()
s.showSon_Name()




'''---------------------------------------------Practice question no - 2----------------------------------
Q2. Vehicle Example

Vehicle class → has attributes like brand and model.

Car class (inherits Vehicle) → adds num_doors.

ElectricCar class (inherits Car) → adds battery_capacity.

👉 Create an ElectricCar object and display all details (brand, model, doors, battery).
'''


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def getVehicle_detail(self):
        print(f"The brand of the car is : {self.brand} and model of the car is : {self.model}\n")


class Car(Vehicle):

    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def showCar_detail(self):
        print(f"The number of door in the car is : {self.num_doors}\n")


class ElectricCar(Car):
    
    def __init__(self, brand, model, num_doors, battery_capacity):
        super().__init__(brand, model, num_doors)
        self.battery_capacity = battery_capacity

    def showElectricCar_detail(self):
        print(f"The battery capacity of the electric car is : {self.battery_capacity} maH \n")

e = ElectricCar("BMW", "32SUP", 2 , 1000000)
e.getVehicle_detail()
e.showCar_detail()
e.showElectricCar_detail()




'''---------------------------------------------Practice question no - 3----------------------------------

Q6. Employee Management

Employee class → attributes name, id, salary.

Manager class (inherits Employee) → adds department.

SeniorManager class (inherits Manager) → adds years_of_experience.

👉 Create a SeniorManager object and display all details using methods.
'''

class Employee:
    def __init__(self, name, id , salary):
        self.name = name 
        self.id = id
        self.salary = salary
    
    def showEmployee_details(self):
        print(f"The name of the employee is : {self.name}")
        print(f"The id of the employee is : {self.id}")
        print(f"The salary of the employee is : {self.salary}")

class Manager(Employee):
    def __init__(self, name, id , salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def showManager_details(self):
        print(f"The department of the manager is : {self.department}")

class SeniorManager(Manager):
    def __init__(self, name, id , salary, department, year_of_Exp):
        super().__init__(name, id , salary, department)
        self.year_of_Exp = year_of_Exp
        
    def showSeniorManager_details(self):
        print(f"The year of experience of the senior manager is : {self.year_of_Exp}")

s = SeniorManager("Rajiv", 9, 124000 , "Ai/ML" , 40)
s.showEmployee_details()
s.showManager_details()
s.showSeniorManager_details()
