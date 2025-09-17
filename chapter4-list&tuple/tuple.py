'''
NOTE : TUPLE 
    --> tuple is an ordered , immutable collection of items.

    FEATURE :
     
    1) The items have a defined order, and that order will not change 
    2) Once they are created, we cannot modify(add,remove or change) items
    3) It is faster than list since it is immutable
    4) Same value can appear more than once 
    5) we can store different data types

    SYNTAX : tuple = () --> This is called empty tuple 
            tuple = (32,) --> This is called tuple with a single element
             NOTE: tuple = (32) ❌ this is show returnType i.e; int
'''

'''
Some methods of tuple that is mostly used :
    1)count(value) => returns how many time the value appears in the tuple 
    2)index(value,start=0, end=len(tuple)) => Returns the index of the first occurence of a value
    3)len(t) => finds the length of the tuple
    4)min(t) / max(t) => smallest/largest element (useful in stats)
    5)sum(t) => returns the total no. of elements of tuple items
    6)aorted(t) => returns a sorted list of tuple items .
    7)any(t) / all(t) => boolean checks across tuple elements
            ---> This returns True or False example :
             1) True if at least one element in the tuple is truthy
             2) False if all elements are falsy (0 , "None", "" , False)
'''

# example of count(value) :
tuple = (23, 45, 23 ,43 ,34, 34 ,23, 23, 23,1,1,1,1)
print(tuple.count(1))

#example of index(value) : 
print(tuple.index(34))
print(tuple.index(23,6,12)) # this format is used for explicit index finding 

#example of len(t) :
print(len(tuple)) # output : length of tuple is 0 - 12 i.e; 13

#example of min(t)/max(t) :
print(max(tuple))
print(min(tuple))

#example of sum(t) :
print(sum(tuple))

#example of sorted(t) :
print(sorted(tuple))

#example of any(t) / all(t) :
print(any(tuple))
print(all(tuple))
