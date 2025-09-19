#NOTE : The concept of for loop is same as in other programming language 
# but syntax is different.

'''
SYNTAX :
for i in range(0,n)             n = 1,2,3.....
    print(i)
'''

#--------------------------------------------------------------
#              PROPERTIES OF (for loop) :
#--------------------------------------------------------------

'''
1) for loop can be used with tuple, list and strings.
2) for loop always works from 0 to n-1 .
3) for loop can also be used with syntax(start, stop, step-size)
        NOTE: step-size is basically interval for the loop continuity
        eg: like if step-size is 2 then 0 -> 2 -> 4 -> 6 .......
   NOTE: (step-size) is not used much    
 
'''

#  EXAMPLE NO : 1 

'''

tuple = (1, "rajiv", 1.3, False, True)
for i in range(0,4):
    print(tuple[i])


'''

#  EXAMPLE NO : 2

'''

numberlist = [0, 1, 2, 3, 4, 5, 6]
for i in range(0, 6, 2):
    print(numberlist[i])

'''

# Write a program to print the multiplication table of 2 using for loop 

'''
for i in range(1,11):
    print("2 X ", i , "= ",2*i)
'''

#NOTE: iteration method of forloop()
'''
--> if we want to print all the element of the list and tuple one by
    one then this two iteration methods are used.

    *) method 1 :
      l = [1, 2, 6, "rajiv",True]
      for i in l:
      print(i)

    *) method 2 :
      t = (1, 2, 6, "rajiv",True)
      for i in t:
      pritn(i)

'''
#--------------------------------------------------------------
#           Most important feature of for loop 
#--------------------------------------------------------------
'''
 NOTE: we can use for loop with (else statements)
 --> The control flow goes to this else statements when the for loop is 
     completely executed (exhausts)
'''

"""------------------ EXAMPLES : ------------------------- """
l = [1, 2, 6, "rajiv",True]
for i in l:
      print(i)

else:
      print("\nThis is the use of else statement's messages")
