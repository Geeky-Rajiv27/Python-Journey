'''
NOTE: ways to open a file in python : 

    method - 1 :

 fileVariable = open("fileName.txt", "mode")     NOTE: by default mode = read i.e; (r)
 fileVariable.read() or f.write("content" or variable that contain content)
 fileVariable.close()

    method - 2 :

 with open("fileName.txt", "mode") as fileVariable :
        fileVariable.write("content")
        print(f.read())

NOTE: here no need to close the file in this method , this automatically 
    closes the file once it is read or write

    Q) how does the compiler or interpreter knows that at which moment
      it have to close the file ?


'''
'''
#-----------------------------------------------------------------------
            Methods to read the file 
#-----------------------------------------------------------------------
1) f.read()     = reads the while file 
2) f.readline() = reads a single line one after another
3) f.readlines()= reads list of all lines




'''

with open("text.txt", "w") as f:
    f.write("hey rajiv are you feeling low ?\n" \
            "This is second line \n" \
            "This is third line")
    
    #method - 2 to read file
with open("text.txt", "r") as f:
    line1 = f.readline() # this gives first line
    line2 = f.readline()    # this gives second line 
    line3 = f.readline()    # this gives Third line
    print(line1)
    print(line2)
    print(line3)


    #method - 3 to read file
with open("text.txt") as f: # this is bydefault readmode
    newlist = f.readlines()
    print(newlist)

'''
#-----------------------------------------------------------------------
   2. File Modes
#-----------------------------------------------------------------------

Know the different modes you can use in open():

Mode	                Description
"r"	            Read (default) = error if file doesn’t exist
"w"	            Write = overwrites the file or creates new
"a"	            Append = adds new data at the end
"x"	            Create = error if file exists
"b"	            Binary mode (e.g., images, videos)
"t"	            Text mode (default)
 +	            Read + Write (e.g., "r+", "w+")
"rb"            Read in binary
"rt"            Read in text
#-----------------------------------------------------------------------
'''

#-----------------------------------------------------------------------
#                   working with images using file handling
#-----------------------------------------------------------------------
'''
--> This is useful for audio , images and pdfs etc
'''
#NOTE: copying image from one file to another file

# sourcefile name : randomImg.jpeg
# destinationfile name : copied.jpeg

with open("randomImg.jpeg", "rb") as original:
    with open("copiedImg.jpeg", "wb") as copy:
        copy.write(original.read())