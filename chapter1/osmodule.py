"""
🔹 Why do we use this?

We use this because:
1)Computers organize data into files and directories (folders).
2)As programmers, we often need to inspect, read, modify, or manage files inside 
directories.
3)os.listdir() and other os functions give us programmatic access to the file system.

Example:
Instead of manually checking 1000 files in a folder, you can write a script to loop through all of them and process automatically.


🔹 Applications in real life

1)File management systems

-->Backup tools, file explorers, or software that scans folders.

2)Data processing

-->If you have a folder full of .csv or .txt files, you can loop through and
 analyze them automatically.

3)Automation scripts

-->Automatically cleaning old logs, renaming files, or organizing downloads.

4)Web development / AI / ML

-->In Machine Learning, you often load datasets stored in directories (like images in train/ and test/ folders).

5)System utilities

-->Antivirus programs scan all files inside a directory structure.

6)Deployment

-->DevOps engineers use such scripts to check directories before deploying applications.



🔹 How often is it used?

Very common in automation, data science, backend development, and DevOps.

For a beginner, you may not use it every day.

For a professional, directory and file handling are core tasks:

Backend developers handle file uploads/logs.

Data scientists read datasets from folders.

System administrators automate directory scanning.

So, it is one of the fundamental tools in Python programming.
"""

##############################################################
#.   ways to use os module and see directories.
##############################################################
import os

# directly assign the directory path (no input())
directory = "/Users/bheshu/Documents"

# list all files and directories in the given path
contents = os.listdir(directory)

print(f"\nContents of '{directory}':")
for item in contents:
    print(item)
