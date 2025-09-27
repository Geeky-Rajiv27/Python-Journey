def myFunc():
    print("hello world ! from function moduleFile = module.py")

if __name__ == "module":  # this is true if this module.py will run directly via this file

#if __name__ == "__module__"    ---> This won't be executed since this program is not 
                # imported from other programs
    myFunc()
