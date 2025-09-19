#NOTE : The concept of while loop() is same as in other programming languages
# but the syntax is different .
'''
In python, there are basically two types of loops :
 1) while loop()
 2) for loop()
'''

'''
--> SYNTAX :
    i = initialize with any value ;
   while(condition):
       loop body
'''

#--------------------------------------------------------------
#              working of while loops() with list
#--------------------------------------------------------------
list = [1, "harry", "Rajiv" , 2.4, True, False, ""]
i = 0 ;
while(i < len(list)):
    print(list[i])
    i = i + 1 
