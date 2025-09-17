#write a program to store seven fruits in a list entered by the user.

'''

f1 = input("Enter the name of first fruits : ")
f2 = input("Enter the name of second fruits : ")
f3 = input("Enter the name of third fruits : ")
f4 = input("Enter the name of fourth fruits : ")
f5 = input("Enter the name of fifth fruits : ")
f6 = input("Enter the name of sixth fruits : ")
f7 = input("Enter the name of seventh fruits : ")
#creating a list 
fruits_list = [f1,f2,f3,f4,f5,f6,f7]
print(fruits_list)
#NOTE: we can also do this by appending after each fruits name entry in the list 

'''

#write a program to accept marks of 6 students and display them in a sorted manner

#first making a list

'''
marklist = []

mark1 = int(input("Enter the marks for student 1 : "))
marklist.append(mark1)
mark2 = int(input("Enter the marks for student 2 : "))
marklist.append(mark2)
mark3 = int(input("Enter the marks for student 3 : "))
marklist.append(mark3)
mark4 = int(input("Enter the marks for student 4 : "))
marklist.append(mark4)
mark5 = int(input("Enter the marks for student 5 : "))
marklist.append(mark5)
mark6 = int(input("Enter the marks for student 6 : "))
marklist.append(mark6)
#also marklist.sort()
#print(marklist)
print(sorted(marklist))
'''

#check that the tuple cannot be changed in python

'''
tuple = (12, 23, 13)
tuple[1] = 12.5  ❌ we cannot assign a new value to the object of tuple 

'''

#   write a program to sum a list with 4 numbers

'''
NumberList = [1,2,3,4,5]
print("Sum of the items of list : ")
print(sum(NumberList))
'''

# write a program to count the number of zeros in the following tuple :

'''
taparey = (1,3,0,5,6,0,30,0,23)
print(taparey.count(0))
'''

