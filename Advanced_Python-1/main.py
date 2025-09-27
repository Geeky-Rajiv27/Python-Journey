'''
------------------------------------------------------------------------------------------------------------
            __main__ (is a builtin python variables that tells the python how the python file is being executed)
            like wether it is executed on it own file which is also called main.py

        NOTE : we can also use it as a condition to check the wether the running program is file itself or 
                is imported from somewhere else
                

        NOTE: if the python.file is executed directly(without importing) then
            __name__ = "__main__"


                eg: if(__name__ == "__main__"):
                        print("This ran directly without importing it from another file")
                    else:
                    print("This is imported from another file")
------------------------------------------------------------------------------------------------------------
'''
from module import myFunc  # ---> output : hello world ! from function moduleFile = module.py

if(__name__ == "module"):# This program is __name__ = module for this program in this file
    print("This ran directly without importing it from another file")
else:
    print("This is imported from another file") # ---> This will be executed since above we have imported so !


myFunc()    # this is to run the function that we have imported form module.py tough we have run already while importing