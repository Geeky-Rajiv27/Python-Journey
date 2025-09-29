'''
Create two virtual environment(env1, env2) , install few packages in the 
first one. How do you create a similar environment in the second one ? 

---> in a following way :

1) first i will create a virtual environment named env1

2) Then second i will create another virtual environment named env2

3) i will activate env1 and install some packages

4) i will store all those packages information to a newly created file (requirements.txt)

5) deactivate env1

6) Then finally , activate env2

7) Clone everything into env2 from that file using [pip install -r requirements.txt]

'''



'''
NOTE : Q2) Write a program to input name, marks and phone number of a student and format it using
        the format function like below :

        "The name of the student is Harry, his marks are 72 and phone number is 99999888"
'''

name = input("Enter your name : ")
marks = input("Enter your marks : ")
phno = int(input("Enter your phone number : "))

formattedString = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phno)
print(formattedString)



'''
NOTE : Q3) A list contains the multiplication tale of 7. Write a program to convert it to vertical
string of same numbers
'''

tableList = [str(7*i) for i in range(1, 11)]
print(tableList)
result = "\n".join(tableList)
print("After conversion : \n")
print(result)