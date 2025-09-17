# write a program to create a dictionary of Nepali words with values as their English
# translation. Provide user with an option to look it up!

'''
dictionary = {
    "jaau" : "go",
    "sanchai_?" : "allgood_?",
    "manxey" : "person",
    "bihey" : "marriage"
}
key = input("Enter the word for which you want meaning in English : ")
print("Meaning of ",key,":",dictionary.get(key))
'''

#write a program to input eight numbers from the user and display all the unique numbers(once)

#creating list to store some repititive items

'''
list = []
element1 = int(input("Enter the element 1 : "))
list.append(element1)
element2 = int(input("Enter the element 2 : "))
list.append(element2)
element3 = int(input("Enter the element 3 : "))
list.append(element3)
element4 = int(input("Enter the element 4 : "))
list.append(element4)
element5 = int(input("Enter the element 5 : "))
list.append(element5)
element6 = int(input("Enter the element 6 : "))
list.append(element6)

#collecting only unique elements from the list by type conversion 
uniqueElements = set(list)
print("only unique elements from the above list : ",uniqueElements)

'''

#Create a empty dictionary then allow 4 friends to enter their favourite language as value and 
# use key as their names.  Assume that the names are unique.

'''


loveLanguage = {}       # this is empty dictionary
name1 = input("Enter your name : ")
language1 = input("Enter the language you like : ")
loveLanguage.update({name1:language1})
name2 = input("Enter your name : ")
language2 = input("Enter the language you like : ")
loveLanguage.update({name2:language2})
name3 = input("Enter your name : ")
language3 = input("Enter the language you like : ")
loveLanguage.update({name3:language3})
name4 = input("Enter your name : ")
language4 = input("Enter the language you like : ")
loveLanguage.update({name4:language4})

print(loveLanguage)

#NOTE (CASE-1): if two friends got same name but has different favourite languages then the dictionary
# at the end will show the recent updated key-value and previos one will be terminated.
#NOTE (CASE-2): and if both the key-value is same as of other friend then one will be terminated.
#NOTE (CASE-3): if the value is same but key is different then no problem it will be accepted
'''




