'''
-----------------------------------------------------------------------------------------
write a program to read the text from the given file 'poems.txt' and find out
 wether it contains the word "their"
-----------------------------------------------------------------------------------------

'''

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
-----------------------------------------------------------------------------------------
        Write a program to generate a multiplication table from 2 to 20 and write it in a
          different files and also place these all files in a folder. 
-----------------------------------------------------------------------------------------
'''

import os

#current directory is :
currDir = os.getcwd()
print(f"Our current working directory is {currDir} \n")
print("Making a new directory \n")


#making a directory to store files that is going to contain multiplication tables
dirName = input("Enter the name of the directory you want to set : ")
os.mkdir(dirName)
print(f"New directory with the name {dirName} is created successfully \n")

#changing path to the directory that we just created:
os.chdir(dirName)
print(f"We are now in a directory is just created with name {dirName} \n")


def tables(n):
    table = ""
    for i in range(1,11):
        table = table + f"{n} X {i} = {n*i} \n"

    #getting directory path
    fullpath = os.path.join(os.getcwd(),f"table_{n}.txt")
    
    with open(fullpath, "w") as f:
        f.write(table)

#calling function 
for i in range(1,21):
    tables(i)



'''
-----------------------------------------------------------------------------------------
        A file contain a word "Donkey" multiple times. You need to write a program which
         replace this word with #### by updating the same file
-----------------------------------------------------------------------------------------
'''


# opening a file in a reading mode 
with open("Donkey.txt","r") as readFile:
   content =  readFile.read()

replacedContent = content.replace("donkey", "######")
print(replacedContent)

#writing replace content in a same file
with open("Donkey.txt", "w") as writeFile:
   writeFile.write(replacedContent)



'''
-----------------------------------------------------------------------------------------
    You will be given a list of words that need to be censored from the content of file

censor_words = ["bad", "ugly", "stupid", "fool", "hate", "dumb", "nonsense", "idiot", "lazy",
 "weak"]
-----------------------------------------------------------------------------------------
'''

censor_words = ["bad", "ugly", "stupid", "fool", "hate", "dumb", "nonsense", "idiot", "lazy", "weak"]

with open("censorWords.txt","r") as readFile:
   Content =  readFile.read()

replacedContent = Content 
for word in censor_words:
    replacedContent = replacedContent.replace(word, "######")
   
print(replacedContent)

#writing replace content in a same file
with open("censorWords.txt", "w") as writeFile:
   writeFile.write(replacedContent)



'''
-----------------------------------------------------------------------------------------
    write program to find no. of the line that contain word "python"
-----------------------------------------------------------------------------------------
  '''


with open("log.txt", "r") as readFile:
     AlllineContent = readFile.readlines()

lineNo = 1
for line in AlllineContent:
     if("python" in line.lower()):
          print(f"yes, python is present in a line no.{lineNo}")
          break
     lineNo += 1   
     
else: #this block will be executed only if for loop is completely executed
    print(f"No, there is no python")  
    
     
'''
-----------------------------------------------------------------------------------------
    write a program to check if the content of one file matches content of another file
-----------------------------------------------------------------------------------------
'''

with open("Donkey.txt", "r") as readFile:
    content1 = readFile.read()
    with open("test.txt", "r") as readanotherFile:
        content2 = readanotherFile.read()
        
if(content1 == content2):
    print("Yes, the content of both files are identical")

else:
    print("No, the content of both files aren't identical")
