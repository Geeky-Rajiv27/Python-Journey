'''
-----------------------------------------------------------------------------------------
write a program to read the text from the given file 'poems.txt' and find out
 wether it contains the word "their"
-----------------------------------------------------------------------------------------


with open("/Users/bheshu/Documents/PythonFull/chapter09-filehandling/poems.txt", "r") as readFile:
    fileContent = readFile.read()
    print(fileContent)  # reading poems 
    print("\n")
    #checking if the file contain the word "readFile"
    if "their" in fileContent:
        print(f"Yes, file contain the word \"their\" ")
    else:
        print(f"No, file doesn't contain the word \"their\" ")

'''



