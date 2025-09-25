'''
NOTE:
Sometimes we need to control the pointer position while reading or writing 
fils which makes reading and writing of file faster and efficient

ways to do:
 --> For this purpose we use special built-in functions like 
    tell() : this tells the current position of the file reading cursor just 
            after writing or reading.
    
    seek(position): helps us to move the positon of the reading pointer cursor
                according to our will
'''

with open("test.txt", "w") as fileforWrite:
    fileforWrite.write("Hello rajiv how are you ?")
    print(f"The position of the cursor after writing above content is : {fileforWrite.tell()}")
 # output must be 25

with open("test.txt")as fileforRead:
    fileforRead.seek(5) # position set to 5
    print(fileforRead.read(6)) # 5th to next 5th (means read first 6 characters from 5)