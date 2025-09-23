'''
---------------------------------------------------------------------------------------------------
 NOTE:       BEHAVIOUR OF CONSTRUCTOR IN INHERITANCE :
---------------------------------------------------------------------------------------------------

--> In C++ we need to call the constructor explicitly of any class. BUT in case of python there is no need to do so
    if we use the feature ===   [ super()__init__() ] inside the regular constructor of the child class whose 
    parent class's constructor we want to call. 
'''     

class Student:
    def __init__(self):
        print("Constructor of class Student is invoked successfully executed !")

