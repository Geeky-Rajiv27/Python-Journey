'''
----------------------------------------------------------------------------
            working with CSV file in python
----------------------------------------------------------------------------
--->Reading CSV (Comma-Separated Values) files is crucial in Python for
     several key reasons, especially in data science, automation, and 
     general programming tasks. The importance stems from CSV's simplicity,
     universal compatibility, and its widespread use for storing tabular data.

     some CSV files that we read are :
         1)Weather and sensor data
         2)Educational and student record
         3)Excel data
         4)Customer and sales data

The built-in csv module:

For basic needs, Python's standard library includes the csv module.
 It provides two main objects for reading: 

    a)csv.reader(): Reads each row as a list of strings. 
        It is memory-efficient and ideal for processing files one row at 
            a time, especially for very large datasets.

    b)csv.DictReader(): Reads each row as a dictionary, using the first row
        of the CSV as the keys. This is very convenient for accessing data by
            column name instead of by index. 


'''

'''
----------------------------------------------------------------------------
            example to write data in CSV file 
----------------------------------------------------------------------------
'''

import csv # importing csv module 

# write CSV
with open("data.csv", "w", newline="") as f:    # newline="" ensures that rows are not separated
                                        # by any newlines in between
    writer = csv.writer(f)  #csv.writer is an object of file that helps to write data in a file
    #                                                               in a CSV format data
    writer.writerow(["Name", "Age"])    #writer is just a variable 
    writer.writerow(["Rajiv", 20])
    writer.writerow(["Samir", 21])


'''
----------------------------------------------------------------------------
            example to read CSV file using CSV_reader() function
----------------------------------------------------------------------------
'''
# no need to import csv ,since already doen above before writing
from csv import reader

with open("data.csv", "r") as rf:
    csv_reader = reader(rf)
    for row in csv_reader:
        print(row)