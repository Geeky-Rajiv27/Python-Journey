#NOTE : Dictionary is also a collection of objects in the form of keyvalue 
#       pair. eg : {"key", "value"}

'''
SYNTAX : 
 
     dict = {
    "name" : "Rajiv",
    "age" : 19,
      "gender" : "male"
}

'''

'''
Features of Dictionary :
  1) It is unordered
  2) It is mutable
  3) It is indexed 
  4) Cannot contain duplicate keys.
'''


'''
Methods() of Python DICTIONARIES :
 
 1)dict.keys() => This returns all keys of the dictionary
 2)dict.values() => This returns all values of the dictionary
 3)dict.items() => returns key-value pairs in the form of tuple 
 4)dic.get(key, default = None) => safely accessing values of keys without any error
 5)dic.update({key : value}) => this adds if not available in dict while updates it's keys if exist
 6)dict.pop(key, default) => it shows value of the key for the last time and deletes from dict
 7)dict.popitem() => Removes and returns the last inserted key-value pair
 8)dict.setdefault(key, default) => get value if key exists, otherwise insert it with default
 9)dict.clear() => Removes all items from the dictionary
 10)dict.copy() => shallow copy of dictionary (useful before modifications)

 '''

dict = {
    "name" : "Rajiv",
    "age" : 19,
      "gender" : "male"
}

#example of dict.keys() :
print(dict.keys())

#example of dict.values() :
print(dict.values())

#example of dict.items() :
print(dict.items())

#example of dict.get(key, default - None) :
print(dict.get("gender")) # if key is not available in the dictionary it will show none

#example of dict.update({key : value}) :
print(dict.update({"major":"CS"})) # this will add to the dictionary since the given keyvalue
print(dict) #                                                             pair doesn't exists
print(dict.update({"name" : "Rajiv_Chaudhary"}))
print(dict)# this will change the name from "rajiv" to "Rajiv_Chaudhary"

#example of dict.pop(key, default) :
print(dict.pop("major")) # this shows corresponding value of key if already exist in the dictionary
print(dict) # this show dictionary after poping that particular key-value pair
print(dict.pop("number", "doesn't_exist")) # this will show doesn't exist since there is no number

#example of dict.setdefault(key, default) :
print(dict.setdefault("GPA", 3.34)) # shows value if key exist otherwise, insert into dictionary
print(dict)

#example of dict.clear() :
dict.clear() # this just clear everything but don't show anything on console 
print(dict)  # we need to use this to check the dictionary if .clear() worked or not?

#example of dict.copy() :
newdict = dict.copy()   # this new dictionary has it own separate memory location tough it is a 
#                                                                                        copy
print("New dictionary : ",newdict)


