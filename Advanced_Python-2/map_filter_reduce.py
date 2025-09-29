'''
NOTE : #Map function : It is basically used whenever we work with different elements of 
        any iterable things. Like list, tuple and sets

        This is mainly used with function : that function can be normal function or
                lamda functions


'''

l = [1, 2, 3, 4, 5]

square = lambda x: x**x
squaredList = list(map(square, l))
print(squaredList)



'''
NOTE : Filter() :   Filter is the method to actually filter the elements from itereables
            based on specified conditions.

        syntax :        filter(function, sequence)

        function : a function that returns true or false for each elements
        sequence : list, tuple and sequence
'''

# program to print filter only square of even number form the list of mix numbers


l = [1, 2, 3, 4, 5]
# lamda function runs for each elements of the above list
squaredList = list(filter(lambda x : x % 2 == 0, l))        # if condition satisfied then 
print(squaredList)  #       elements is kept otherwise not taken



'''
NOTE : Reduce() : The reduce() function in Python is used to apply a function cumulatively to 
the items of a sequence, reducing it to a single value. Unlike map() or filter(), which return
 sequences, reduce() returns a single result.

NOTE : reduce() is not a built-in function in Python 3; you need to import it from the 
        functools module. eg : from functools import reduce

                    reduce(function, iterable, initializer)

NOTE : initializer (optional): A starting value. If provided, it’s used as the first argument
         in the first call.                    
'''

'''
# program to find the maximum value from a list of numbers
'''
from functools import reduce
allnum = [1, 3, 5, 3, 6, 4, 4]

maxnum = reduce(lambda x,y: x if (x > y) else y, allnum)
print(maxnum)