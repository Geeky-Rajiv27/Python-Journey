'''
    Q)What is os module in python ?
    ans.    
        os module is the special type of built In library in python that allows programmers to 
        interact with the operating system like manipulation with directories , 
        process management and environment variable.

 way to use :  
            1) to use this we need to import it first using (import os)
            2) There are many (os objects) in os module

'''

'''
--------------------------------------------------------------------------------
            File and Directory Operations with (os module)
--------------------------------------------------------------------------------

1)os.mkdir(path)    = this allows to make a new directory
2)os.rmdir(path)    = this allows to delete an empty directory only
3)os.getcwd()       = this provides current directory path
4)os.remove(path)   = this deletes a file 
5)os.rename(source, destination) = renames a file or folder
6)os.listdir(path)  = returns list of all directories
7)os.chdir(path of directory to which you want to change) = changes the current working directory
8)os.path() :   
            Is a submodule that provides various functions for manipulation like :
            a)os.path.exists() : to check if file of given path exists already or not
            b)os.path.join()   : 
            c)os.path.basename() :
            d)os.path.dirname() :
'''

'''
--------------------------------------------------------------------------------
Environment Variables:
--> "Environment variables are variables provided by the operating system that store important 
    configuration data, such as system paths, user settings, or application secrets
      (like API keys or passwords, if the user chooses to set them)."
--------------------------------------------------------------------------------

        os.environ:

          A dictionary-like object that provides access to environment variables.
            You can read and modify them using dictionary syntax (e.g., os.environ['HOME']).
--------------------------------------------------------------------------------
 '''
import os
#example to get current working directory
currentDirectory = os.getcwd()
print(f"Current directory is {currentDirectory} \n")

#example to create a new directory in a current working directory
directoryName = input("Enter the name of the directory you want to set : ")
os.mkdir(directoryName)
print("\n")
print(f"New directory with name {directoryName} is created \n")

#example to delete an empty directory

# os.rmdir(directoryName)  
''' this won't let program to create a directory 
#       since it deletes the newly created directory but without this 
# new directory can be created
'''

#example to move into the currently created new directory so we can create file   
#inside it.
os.chdir(directoryName)
print(f"Directory is changed to {directoryName} \n")
print(f"Current directory is {os.getcwd()} \n")


#example to create a file inside that newly created directory
fileName1 = input("Enter the name of first file : ")
fileName2 = input("Enter the name of second file : ")
with open(fileName1, "w") as file1:
    file1.write("hey i just created a file inside that newly created directory \n")
    print("Content in first file is successfully written inside the file\n")

with open(fileName2, "w") as file2:
    file2.write("This is the file which is not required so better delete this file\n")
    print("Content in second file is successfully written\n")
    print(f"Current directory is : {os.getcwd()}\n")

#changing to directory where file is created
latestdir = os.getcwd()


#example to see the list of files that we just created created
print("Files in the current directory : ")
for files in os.listdir(latestdir):
    print(files)
print("\n")

#deleting the file which is named (notIMPfile)
deletingfileName = input("Enter the name of file you want to delete : ")
if(os.path.exists(deletingfileName)):
    os.remove(deletingfileName)

else:
    print(f"{deletingfileName} is not found inside newly created {directoryName}\n")

#remaining file in the directory after deleting the file we wanted to delete
for leftfile in os.listdir(latestdir):
    print(leftfile)