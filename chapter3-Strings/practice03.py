# write a python program to display a user entered name followed by good afternoon using input() function

#new method (fstrings)

# name = input("Enter your name : ")
# print(f"Good Afternoon {name}")


#write a program to fill in a letter template given below with name and date.

# letter = '''
#             Dear <|Name|>,
#             You are selected!
#             <|Date|>
# '''

# print(letter.replace("<|Name|>", "Rajiv").replace("<|Date|>", "17 sept"))

#write a program to detect double space in string .

string = "hello  Rajiv"
# print(string.find("  "))


#write a program to detect doube space by a single space from problem 3

# print(string.replace("  ", " ").find(" ")) 
#NOTE : here the strings are immutable which means you cannot change them by 
#running functions on them (means string change hudaina but ysley auta new)
#(string banauxa jasma single whitespace hunxa actual wala change hudaina )
# we can say it makes copy of the original and then perform and prints output


