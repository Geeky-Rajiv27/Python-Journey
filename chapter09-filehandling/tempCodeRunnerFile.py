lineNO = 0
with open("log.txt", "r") as readFile:
     for line in readFile:  # file object like here(readFile) in python are natural iterator that   
        # that provides a single line at a time if kept under loops. SO while checking we can use 
        # "line" in the condition it actually contains a single line content at a time
        if("python" in line.lower()):
            lineNO += 1
        
print(lineNO)
    