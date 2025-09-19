#write a program to find the greatest number among 3 numbers using function



def greatest(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3
    
result = greatest(4,2,7)
print(f"{result} is the greatest number")



#---------------------------------------------------------------------------------


#write a program for converting temperature  celcius to fahrenheit using
# function


def tempConverter(cel):
    return 1.8*cel + 32.0

cel = float(input("Enter the temperature in celcius : "))
fah = tempConverter(cel)
print(f"{cel:.2f} ℃  = {fah:.2f} ℉ ")     # :.2f is used to set precision of .2 decimals



#---------------------------------------------------------------------------------


# write a recursive function to find calculate the sum of first n natural number


def sumNatural(n,i,sum):

    if(i > n):
        return sum
    else:
       return sumNatural(n,i+1,sum+i)


n = int(input("enter the value of n : "))
result = sumNatural(n,1,0)
print(f"{result} is the sum of first {n} natural number")


#---------------------------------------------------------------------------------


#write a python program to print n lines of below pattern
'''
* * * 
* *
*
'''

n = int(input("Enter the numbers of line : "))
for j in range(0,n):
        print("*"*(n-j), end="")  #stays in same line
        print("")   #next line  



#---------------------------------------------------------------------------------


#write a python function that converts inches to cms


def unitConversion(inches):
    return 2.54 * inches

inches = float(input("Enter the value of inches : "))
result = unitConversion(inches)
print(f"{inches:.2f} inch = {result:.2f} cm")


#---------------------------------------------------------------------------------


#write a python function to remove the word(pro) from the list and strip at the same time

'''
⚡ Key difference:

strip("pro") → removes any combination of "p", "r", "o" from start and end only.

replace("pro", "") → removes the exact substring "pro" from anywhere.
'''
def removeWord(word, list):
    # making a new list for storing condition based items only
    newlist = []
    for listItem in list:
       if not (listItem == word):
           newlist.append(listItem.replace(word,""))
           # for eg: rajiv is not equal to word so it will append stripped rajiv which is same
           # no change since in rajiv there is no "pro" so same "rajiv" will be appended in 
           # newlist.but for "pro" will won't append that in new list 
    return newlist
           

list = ["rajiv", "proNoobsamir", "amanNOOBpro", "pro"]
print(removeWord("pro", list))

#---------------------------------------------------------------------------------

#write a python function to print the multiplication table of the given number 

def table(n):
    for i in range(1,11):
        print(n," X ",i," = ",n*i)


n = int(input("Enter the number for which you want table : "))
table(n)
