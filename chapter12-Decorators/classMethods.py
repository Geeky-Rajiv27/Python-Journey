'''
NOTE:   classmethod is a special type of decorators that allow the make changes in the class
        level of attrubutes. Since it is shared by all objects.

        --> They are shared by all objects 

        --> They can be called by object and className both

        --> Generally (cls) is used instead of self.
'''
#NOTE: EXAMPLE : 

class decoratorEg:
    a = 1       #   a  is a class attributes (it is shared by all objects)

    @classmethod
    def classMethod(cls):
        print(f"The value of a is : {cls.a}")

#using object
obj = decoratorEg()
obj.a = 5 
obj.classMethod()   #---> This will only show 5 that is instance attribute if @classmethod is not used


#NOTE: in case i just only want to get class value then i have to use decorator "@classMethod"
'''--> Now, this will give me class value no matter i call after changing the method's value '''


