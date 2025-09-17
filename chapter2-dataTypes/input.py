# NOTES : points to remember about input() functions in python

# 1) input are special funcitons used to get input .
# 2) input funcitons are like prompt() that we use in javascript 
# 3) data taken via input is always string .So we need to make this first into the type
    # we want using type conversions 

##########
#EXAMPLE : this will show what if we don't use type conversion while using input() functions
# and perform arithematic opeartions 

a = int(input("Enter the value of num1: ", ))
b = int(input("Enter the value of num1: ", ))
print("Sum of num1 and num2 is : ", a+b)

