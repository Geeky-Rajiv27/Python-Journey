'''
1) write a program to print multiplication table of a given number using 
    for loop.

number = int(input("Enter the number for which you want a table : "))
for i in range(1,11):
    print(number," X ",i," = ",number*i)
'''

#-----------------------------------------------------------------------

'''
2) write a program to greet all the person names stored in a list "l"
    and which starts with S
Given list :
        l = ["Harry","Soham","Sachin","Rahul"]
l = ["Harry","Soham","Sachin","Rahul"]
for i in range(0,len(l)):
    if(l[i].startswith("S")):
        print("Hello ",l[i])
'''

#-----------------------------------------------------------------------


'''
3)Attempt problem 1 using while loop.(mullitplication table)
num = int(input("Enter the number for which you want multiplication table :"))
i = 1
while(i < 11):
    print(num," X ",i," = ",num*i)
    i = i + 1 

    '''
#-----------------------------------------------------------------------

'''
#write a program to find whether a given number is prime or not.


helper = 0
num = int(input("Enter the num to check : "))
if(num == 0 or num == 1):
   helper = 1

elif(num == 2):
    helper = 0
    

elif(num % 2 == 0):
   helper = 1
    
else:

    for i in range(2, (num // 2)+1):
        if(num % i == 0):
            helper = helper + 1
            break

if(helper):
    print(f"{num} is not a prime number")

else:
    print(f"{num} is prime number")

'''
#-----------------------------------------------------------------------
'''
write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter the value of n : "))
i = 0
while(i <= n):
    i = i + 1
   
print(i)

'''

#-----------------------------------------------------------------------

'''
write a program to calculate the factorial of a given number usign for loop

num = int(input("Enter the number for which you want factorail : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i    

print(f"{fact} is the factorial of the {num}")

'''

#-----------------------------------------------------------------------
'''
write a program to print the following star pattern

  *
 ***
*****

// method 1 
rows = int(input("Enter the no. of rows : "))
for i in range(1,rows + 1):
        print(" "*(rows-i), end="") #end="" helps us to prevent the print() 
        print("*"*(2*i-1), end="") #form giving new line by default
        print("") # no need to use "\n" cuz print("") gives newline bydefault

#method - 2

rows = int(input("Enter the no. of rows : "))
for i in range(1,rows + 1):
        print(" "*(rows-i) + "*"*(2*i-1), end="")
        print("") 
        
'''

#-----------------------------------------------------------------------
'''
write a program to print below patterns :

*
**
***

row = int(input("Enter the rows : "))
for i in range(1,row+1):
    print("*"*i)
    
'''
#-----------------------------------------------------------------------
'''
write a program to print the following pattern :
* * *
*   *
* * *

* * * * 
*     *
*     *
* * * *

// method : 1 

row = int(input("Enter the row : "))
for i in range(1,row+1):
   if( i == 1 or i == row):     #  for 1st and last row
        for j in range(1,row+1):
            print("*", end="")
        print("") # for new line 
        
   else:
        for j in range(1,row+1): # this is for row except 1st and last
            if(j == 1 or j == row):
              print("*", end="")   
            else:
                print(" ", end="")

        print("")   # new line 

        

#NOTE : method : 2

row = int(input("Enter the row : "))
for i in range(1,row+1):
    if(i == 1 or i == row):
        print("* "*(row))    # this after symbol it will provide newline by default

    else:
        print("* " + "  "*(row-2) + "*")
    
'''
#-----------------------------------------------------------------------
''' 
write a program to print multiplication table of n using for loops in reversed
order.
'''
num = int(input("Enter the num for which you want table : "))
for i in range(10,0,-1):        #here 0 means 0+1 = 1 i.e; fro (10 to 1) 
    print(f"{num} X {i} = {num * i}")

    
      
      
      