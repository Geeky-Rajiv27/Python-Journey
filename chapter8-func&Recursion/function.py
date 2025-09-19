'''
#NOTE : function is a piece of code (block of code) that solves the specific part of the program
  THis helps us to solve big problems by solving them in chunks

  ---> The concept of function is same as in other programming languages but it is different
        syntax wise.

        There are two types of function in python :
         1) built in funciton : len() , range() , print()
         2)userdefined function : user gives the name of the function on their own and 
                defined what they needs to do themselves.

        SYNTAX :

        def function_Name(parameter1, parameter2,......):       -=-> function definition
             func body 

        function_Name(argument1, argument2,......) ---> function calling                
                
'''

'''
-----------------------------------------------------------------------------------------
#                               Recursion
-----------------------------------------------------------------------------------------

---> Recursion can be defined as the type of function that call itself again and again
        untill and unless the condition , given by user is not satisfied.        

NOTE : The programmer needs to be extemely careful while working with recursion to
        ensure that the function is not calling itself for infinite no. of time .This 
        is used because sometime Recurson is the best direct way to solve the problem.
        
        '''

# example of a program to find factorail of a given number (n) using recursion 

'''
def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1)
    
n = int(input("Enter the number : "))
result = fact(n)
print(f"{result} is the factorail of {n}")

'''
