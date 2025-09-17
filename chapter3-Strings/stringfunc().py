"""
-----------------------------------------------------------------------
1. Case Conversion
-----------------------------------------------------------------------


str.upper() → Converts all characters to uppercase.

str.lower() → Converts all characters to lowercase.

str.title() → Converts the first character of each word to uppercase.

str.capitalize() → Capitalizes the first character of the string.

str.swapcase() → Swaps uppercase to lowercase and vice versa.

-----------------------------------------------------------------------
2. Searching & Checking
-----------------------------------------------------------------------

str.find(sub) → Returns the index of the first occurrence of sub (or -1 if not found).

str.index(sub) → Same as find but raises an error if not found.

str.startswith(prefix) → Returns True if the string starts with prefix.

str.endswith(suffix) → Returns True if the string ends with suffix.

str.count(sub) → Counts the number of occurrences of sub.

str.isalpha() → Checks if all characters are alphabetic.

str.isdigit() → Checks if all characters are digits.

str.isalnum() → Checks if all characters are alphanumeric.

str.isspace() → Checks if all characters are whitespace.


-----------------------------------------------------------------------
3. Modification & Formatting
-----------------------------------------------------------------------

str.strip() → Removes leading and trailing whitespace.

str.lstrip() → Removes leading whitespace.

str.rstrip() → Removes trailing whitespace.

str.replace(old, new) → Replaces all occurrences of old with new.

str.join(iterable) → Joins elements of an iterable with the string as a separator.

str.split(sep=None) → Splits the string into a list by sep (default: whitespace).

str.rsplit(sep=None) → Splits from the right.

str.partition(sep) → Splits the string into a tuple: (before, sep, after).

str.zfill(width) → Pads the string with zeros on the left to fill width.
-----------------------------------------------------------------------
"""

str = " rajiv is good good man and bad boy "  # Given string is "rajiv"
print(str.upper())   # output : "RAJIV IS GOOD MAN AND BAD BOY"

print(str.lower()) # output : "rajiv is good man and bad boy"

print(str.capitalize()) # output : "Rajiv is good man and bad boy" 

print(str.title()) #output : "Rajiv Is Good Man And Bad Boy"

mixcase = "Hello World 123!"
print(mixcase.swapcase()) #output : "hELLO wORLD 123!"

print(str.find("good")) #output : 9 --> this is the index of the first occuring good in the sentence

print(str.find("none")) # output : -1 --> there is no "none" in the sentence so -1.(not found)

# print(str.index("none")) # output : shows error unlike find() which shows -1 for if not found

print(str.startswith("rajiv")) #output : True (since the starting word in the sentence is rajiv)

print(str.endswith("man")) #output : False (since the ending word in the sentence is boy)

print(str.isalpha()) # output : False (since in the sentence the whitespaces aren't alphabetic (a-z)) 
#eg : it will show true for print("afhur".isalpha()) --since afhur is all alphabetix (a-z) || (A-Z)
print("afhur".isalpha())

print(str.count("good")) #output : 2 (since in the sentence there is good X 2 (twice))

print(str.isalnum())  #output : False (since the sentence are neither alphabetic nor numeric)

print(str.isspace()) # output : False (since there are some charcters words )

print(str.strip()) #output : "rajiv is good good man and bad boy" --> now we can see there is no
#whitestrips(whitespaces)

print(str.lstrip()) #output : "rajiv is good good man and bad boy  " --> only removes the starting 
                    # whitespaces basically (left strips/spaces)

print(str.rstrip()) #output : "  rajiv is good good man and bad boy".  -> removes right side spaces

print(str.replace("good", "smart")) #output :  rajiv is smart smart man and bad boy 

#--------ALL about .join()------------------

#.  1)    LIST OF STRINGS :
words = ["Python", "is", "fun"]     # this is list of objects
#       -> Big braces are used in case of sets of strings 

print("-".join(words))   # Output: Python-is-fun

print(" ".join(words))  #output : Python is fun.  --> this joins the 

text = "rajiv"
print("-".join(text))      #output : r-a-j-i-v. --> python treats the string as single character

#       2) TUPLE OF STRINGS :
#       ->  paraenthesis are used in case of sets of strings 


words = ("apple", "banana", "cherry")
print(", ".join(words))   # Output: apple, banana, cherry


#       3) Sets of Strings : --> order is not guaranteed in output as input in case of this sets of strings
#       -> curly braces are used in case of sets of strings 
#       -> the output sets will be always different

words = {"apple", "banana", "cherry" }
print(", ".join(words))



###--------------------------DIfference between [list of strings] And [tuple of strings]-----#

"""

lst = ["a", "b", "c"]
lst[0] = "x"       # ✅ Works
lst.append("d")    # ✅ Works

tpl = ("a", "b", "c")
tpl[0] = "x"       # ❌ Error: tuples cannot be changed
tpl.append("d")    # ❌ Error


"""

