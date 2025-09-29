'''
NOTE : join method works for the only string so it is also string method.

1)     it is used to concatenate (join) elements of an iterable like (list, tuple and sets)
        No dictionary since it is not iterable as above 3 things 

2)      It is used to concatenate with a specified separator between each elements

----------------------------Syntax: -------------------

            'separator'.join(iterable)

NOTE:   All the elements inside the iterable() must be string and shouldn't be numbers.
NOTE:   to join numbers first we have to convert them into string and then only we can
            join them 

        numbers = [1,2,3]
        result = "-".join(map(str, numbers))
        print(result)       --> Output: 1-2-3
'''

#example : 

a = ["Rajiv", "Richer", "Duffy"]
final_result = "___".join(a)        #--> We can use any type of separators even a (strings)
print(final_result)