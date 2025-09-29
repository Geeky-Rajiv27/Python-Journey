'''
NOTE : Lamda function is a type of function made up of an expression (lamda keyword)
        This work same as regular keywords.


        -------SYNTAX----------

                    function_name = lamda Function_parameters : returning part
f(x) calling -->    function_name(arguments)


'''

#example - 1 
square = lambda x : x**x
print(square(2))      # calling function



#example - 2 
table = lambda num, i : f"{num} X {i} = {num * i}"
i = 1
while(i <= 10):
    print(table(2,i))
    i += 1