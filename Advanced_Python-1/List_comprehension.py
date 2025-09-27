'''
NOTE: List comprehension : It is just a way that allows us to use expression for each 
     iterating items of List-1 and put that result in the newly made List-2.

     --> We can also add some conditions.
     --> This is slightly faster than a normal for loops

    SYNTAX : NewList = [expression for i in range if condition]

NOTE : condition is optional
'''

print("--------------------Without List comprehension-------------")
print("---Creating List of squared items of the List- 1----------------\n")

List_1 = [1, 2, 3, 4, 5]
print(f"List - 1 : {List_1}")
List_2 = []
for item in List_1:
    List_2.append(item * item)

print(f"List - 2 : {List_2}")
print("\n")


print("--------------------With List comprehension-------------")
print("---Creating List of squared items of the List- 1----------------\n")

List_one = [1, 2, 3, 4, 5]
print(f"List - 1 : {List_1}")
List_two = [item * item for item in List_one]
print(f"List - 2 : {List_2}")
print("\n")


print("--------------------With List comprehension-------------")
print("---Creating List of squared items of the List- 1 only which are even------------\n")


List_first = [1, 2, 3, 4, 5]
print(f"List - first : {List_first}")
List_second = [item * item for item in List_first if (item % 2 == 0)]
print(f"List - second : {List_second}")
print("\n")