'''
--------------------------------------------------------------------------------------------------------------
        Exception handling with else block(statements)-----> try with else
--------------------------------------------------------------------------------------------------------------
--> This is just a newly added feature to python to the domain of exception handling
    Here we use an extra block that is (else block) at the end of the try - except

NOTE:   so, the else block is executed ---===---    only if the (try block) doesn't throws an exceptions
       
        the else block is not executed ---===---    only if (try block) throws an exceptions

'''

try:
    age = int(input("enter your age : "))
    
    if(age >= 18):
        print("You are eligible to vote")
    else:
        print("You aren't eligible to vote")
except ValueError as e:
    print(e)

else:
    print("This is inside else. This will be executed if no exception is thown")



 
'''
--------------------------------------------------------------------------------------------------------------
        Exception handling with finally block(statements)-----> try with finally
--------------------------------------------------------------------------------------------------------------

--> This is basically used in functions .
    
    NOTE : This is executed at all cases either try block throws an exception or not 
'''    

try:
    age = int(input("enter your age : "))
    
    if(age >= 18):
        print("You are eligible to vote")
    else:
        print("You aren't eligible to vote")
except ValueError as e:
    print(e)

finally:
    print("This is inside finally. This will be executed at all cases")