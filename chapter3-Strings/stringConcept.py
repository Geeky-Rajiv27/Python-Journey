# this is no difference in the concept of string that we need in python . This is same as other
# programming languages . 

"""-----------------------------------------------------------------------------------

1) here we can see the concept of slicing that we do in js. The concept behind slicing is also same 
    as in js 
2) here we can see the concept of array indexing that we do in C language 
-----------------------------------------------------------------------------------
"""


"""
-----------------------------------------------------------------------------------

SLICE : here one more extra concept in slicing is that there is negative indexing .
 In case of negative slicing concept we count always form back and not form 0 but from -1 and so on
 eg : string = Rajiv ;   negative array indexing : -1,-2,-3,-4,-5.
                         normal array indexing : 0, 1, 2, 3, 4 this is for Rajiv.

    SYNTAX : str[startIndex:lastIndex]
                         """

"""
-----------------------------------------------------------------------------------
                    Syntax for slicing in strings is :


sequence[start : stop : step]


sequence → string, list, tuple, etc.
start → index where slicing begins (default = 0).
stop → index where slicing ends (exclusive, not included).
step → how many steps to jump (default = 1).
-----------------------------------------------------------------------------------
"""
# IMPORTANT NOTES : 

#1) print(str[0:4]) # here character of index 4 is not included . ==.    print(str[:4]) this is same

#2) print(str[1: ]]) # here the empty space means [1:length] ==   print(str[1:5]) this is same

    #. Incase of negative indexing 

# 1) print(str[-4:-1]) --> here the last index's char i.e; index -1 is not included 
  

###---------------------------------------------------------------
###                  Slicing with skip value : 
###---------------------------------------------------------------

"""
here what we get is skip values 
SYNTAX : print(str[_:_:_])  --> the last one is skip value 
"""
"""-EXamples : for advanced slicing techniques
    data = "chaudhary"
    print(data[0:9:1])       #--> output : chaudhary
                            since we used 1 as skip value so it doesn't skips 

    print(data[0:9:2])       #--> output : caday
                             #--> this skip's one character after single interval of character
                             like skip's 'h' and then again after one character i.e; 'a' it again
                             skips 'u' and so on. 

    data = "chaudhary".    #---> output : "cua"
    print(data[0:9:3]) 
"""
###---------------------------------------------------------------
#.              examples :
###---------------------------------------------------------------

str = "Rajiv"
#showing the character j and i only using slice 
print(str[2:4]) 

