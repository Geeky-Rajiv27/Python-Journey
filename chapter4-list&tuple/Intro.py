'''
List = Unlike strings in case of lists are mutable that is we can change 
the object of list using array indexing.

list is mutable : we can append , add  , remove objects of list

NOTE : in string we cannot do such things 

NOTE : slicing of list can be done same as in strings
'''


friends = ["Apple", "Orange", 5, 345.06, False, "Aakash" , "Rohan"]

#as we discussed above we can change the content of each index 
friends[0] = "Banana"
print(friends)

