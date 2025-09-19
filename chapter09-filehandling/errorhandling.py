'''
NOTE: Exception handling in file operations 
---> We should always handle missing files properly in file handling

1) There are lots of built-In exceptions in python that can be used intitutively.
2) "Exception" is the general way to catch the exception but i don't tell the type of exceptions
3) We can use multiple "except" block so that it could catch multiple errors

        List of most useful Builtin exceptions:
  -----------------------------------------------------
1. ValueError
    This exception is fundamental for handling invalid data from user input or external systems.
    It signals that a function has received an argument of the correct type but an inappropriate value.

    Example: 

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! That was not a number.")
  -----------------------------------------------------  
2. TypeError
    As a common error for beginners and experienced developers alike, TypeError is raised
      when an operation or function is applied to an object of an inappropriate type.

    Example: 

try:
    result = "5" + 5
except TypeError:
    print("Error: You can't add a string and an integer.")  
  -----------------------------------------------------   

3. KeyError and IndexError (treated together)
        These two exceptions are essential for data structure lookups and are part of the
          LookupError hierarchy. KeyError occurs when a dictionary key is not found.
        IndexError occurs when a sequence (like a list or tuple) index is out of range. 

    Example:

my_dict = {'a': 1}
my_list = [1, 2, 3]

try:
    print(my_dict['b'])
    print(my_list[3])
except (KeyError, IndexError) as e:
    print(f"Lookup error: {e}")   

  -----------------------------------------------------   
4. FileNotFoundError
        This is a specific, highly useful subclass of OSError that is raised when a file or
          directory is requested but does not exist. Handling it gracefully is a crucial part 
          of robust file I/O.

Example: 

try:
    with open("nonexistent_file.txt") as file:
        file.read()
except FileNotFoundError:
    print("Error: The file could not be found.")
  -----------------------------------------------------  
5. ZeroDivisionError:

    This exception is raised when the second argument of a division or modulo operation is zero. 
    It's a clear and specific arithmetic error.

    Example: 

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Calculation error: Cannot divide by zero.")
  -----------------------------------------------------   




            SYNTAX with Example


'''
try:
    with open("file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
