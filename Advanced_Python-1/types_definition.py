'''
NOTE:   Types : This is an explicit way to specify the varibles with return types.
              in python there is no need to use return types but if required , we can
                use Types features

        SYmbol :       varible_name: datatype = value
        eg :            a:int = 5
'''
a: float = "rajiv"      # here it is expected that a will be float but , i have assigned
# string . Inspite of this a will store the string and won't throw any errors since python
# doesn't care at runtime .
print(a)            # output : rajiv
print(type(a))      # output : <class str>

#NOTE:      This is just a type hint for user(devs) to expect the type of value .
#           this increases the code readability.


'''
--------------------------------------------------------------------------------------------------------------
            Using (type hint - feature) in functions
--------------------------------------------------------------------------------------------------------------
'''

def sum(a: float, b: float) -> int :
    return a+b          # This will return float (tough the hint type is int) since python doesn't care at runtime
    # To get actually in (int) we need to do explicit type casting eg : return int(a+b)
result = sum(1.5,1.44)
print(f"The sum is : {result}")