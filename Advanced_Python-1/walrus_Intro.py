'''
NOTE : Walrus -->   Walrus is a newly added (assignment based) feature in python 3.8 version.
        
        1) This allows us to assign value to variable in the same line where we give conditions. 
                for eg : loops, if cases etc.
        
        2)This is not used mostly but developers use this very less , like when if it is helping to reduce the 
                code.

        3) Many devs avoid this to use specially beginners since it makes code very hard to read.

'''



'''---------------------------------------------------------------------------------------------------------
        SYTNTAX :   :=              --> So this is the symbol of walrus
------------------------------------------------------------------------------------------------------------
'''
#EXAMPLES - 1 :

if(age := int(input("Enter your age : ")) )>= 18 :      #so here what happeining is we are first passing value
    print("Your are eligible to vote")                      #                                and then comparing

else:
    print("YOu are not eligible to vote")

#example 2 :

if(length := len([1, 2, 3, 4, 5, 6])) > 5:
    print(f"length : {length} for the above given list is too long , expected length : 3")
else:
    print(f"length : {length} for the above given list is correct")
