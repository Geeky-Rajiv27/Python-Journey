'''
NOTE:--> Without enumerate method in loop, it is little bit difficult to print the 
        index of the item while printing the items of list one by one using 
        for loop

        But by the help of enumerate method in loop , we can easily do this : 

'''

#without enumerate:
l = ["apple", "banana", "orange"]

index = 0
for item in l:
    print(f"The item of index no : {index} is {item}")
    index += 1

#----------------------------------------------------
print("----------With enumerate methods : -----------------\n")

itemList = ["apple", "banana", "orange"]

for item, index in enumerate(itemList):
    print(f"The item of the index no: {index} is {item}")

