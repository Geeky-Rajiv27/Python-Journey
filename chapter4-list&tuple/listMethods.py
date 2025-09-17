#NOTE: we will apply any function over string then it makes a new string
#       with required changes but incase of list we can change the original
#       list after applying any function over list.

'''
#NOTE:  important methods() for lists :

1) list.sort() = updates the list in ascending order
2) list.reverse() = updates the list to [15,21,2,7,8,1]
3) list.append()
4) lsit.insert(3,8) = This will add 8  at index 3
5) list.pop(index) : by default it will pop out last index element
6) list.remove(element) = will remove particular first occuring element
                     from the list

'''

numberlist = [1,3 ,2.2, 2.1, 5]
# print(numberlist.sort()).     ---> this is wrong way, we cannot do as string
numberlist.sort()
print(numberlist)

numberlist.reverse()
print(numberlist) #--> this will reverse the new sorted list rather than given

numberlist.append(4)
print(numberlist)

numberlist.insert(3,6)
print(numberlist)

numberlist.pop(4)
print(numberlist)

numberlist.remove(4)
print(numberlist) # --> this will remove 4 from the list 
