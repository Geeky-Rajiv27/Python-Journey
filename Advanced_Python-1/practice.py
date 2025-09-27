'''
1) write a program to open three files 1.txt, 2.txt, 3.txt if any of these files doesn't 
    exits then print("Without exiting the program")
'''



try:
    with open("1.txt", "r") as file1, \
         open("2.txt", "r") as file2, \
         open("3.txt", "r") as file3:
        print("File opened successfully !")

except FileNotFoundError as e:
    print("Without exiting the program")


'''
3) Write a list comprehension to print the list that contain multiplication table  of a
    user entered numbers.
'''
num = int(input("Enter the number : "))

table_list = [f"{num} X {item} = {num * item}" for item in range(1, 11)]
print(table_list)