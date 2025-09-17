# Write a program to find the greatest of four numbers entered by the user.

'''

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
num4 = int(input("Enter the fourth number : "))

if(num1 > num2):
    if(num1>num3):
        if(num1>num4):
            print("num1 is greater numbers")

        else:
             print("num4 is greater number")

    elif(num3 > num4):
         print("num3 is greater number")

    else:
         print("num4 is greater number")             

elif(num2 > num3):
        if(num2 > num4):
            print("num2 is greater number")
             
        else:
             print("num4 is greater number")

elif(num3 > num4):
     print("num3 is greater number")

else:
     print("num4 is greater number")      
'''

# write a program to find out whether a student has passed or failed if it requires a total
# of 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input 
# from the user

'''

marks1 = float(input("Enter the marks of science : "))
marks2 = float(input("Enter the marks of Mathematics : "))
marks3 = float(input("Enter the marks of C programming : "))
obt = marks1 + marks2 + marks3
percentage = (obt/300)*100
print("Percentage : ",percentage)
if(percentage >= 33):
    print("Passed")

else:
    print("Failed")    

'''


#A spam comment is defined as a text containing following keywords.
#"Make a lot of money", "buy now", "subscribe this", "click this". Write a program to 
# detect these spams.

'''

s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

text = input("Enter the text : ")
if((s1 in text) or (s2 in text) or (s3 in text) or (s4 in text)):
     print("This msg is a spam")

else:
     print("This is not a spam")     
   
''' 

#write a program to find whether a given username contains less than 10 characters or not

'''
sentence = "rajiv is a good boy"
if(len(sentence) == 10):
    print("sentence contains 10 characters")

else:
    print("sentence doesn't contains 10 characters")
    
'''

#write a program which finds out whether a given name is present in a list or not 

'''
list = ["rajiv", "ram", "krishna"]
name = input("Enter the name : ")
if(name in list):
    print("The name is in list")

else:
    print("Name is not in the list")
'''

# write a program to calculate the grade of a student from his marks from the following scheme:
"""
NOTE: 
90 - 100 -> Ex
80 - 90 -> A
70 - 80 ->B
60 - 70 ->C
50 - 60 ->D
  <50 -> F
"""
'''

mark = float(input("Enter your marks: "))
if(mark >= 90 and mark <= 100):
    print("Grade : Ex")

elif(mark >= 80 and mark <= 90):
    print("Grade : A")

elif(mark >= 70 and mark <= 80):
    print("Grade : B")

elif(mark >= 60 and mark <= 70):
    print("Grade : C ")

elif(mark >= 50 and mark <= 60):
    print("Grade : D")

elif(mark > 100):
    print("Not possible !Please recheck the mark")

else:
    print("Grade : F")
'''

#write a program to find out whether a given post is talking about "Harry" or not.

post = "Harry is smart asf. Harry is very athletic too"
if("Harry" in post):
    print("Post is about Harry")

else:
    print("Post is talking about Harry")
    