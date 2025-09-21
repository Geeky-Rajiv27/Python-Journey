'''
json file : It is nothing but a collection of key-value pair based data 
    that is easy to understand by both machine and human        

    Most web services and APIs (Application Programming Interfaces) use 
    JSON to send and receive information. For example, when your Python 
    application needs to get weather data, stock prices, or social media
    information, it will often communicate with a web server using JSON.
     Python's built-in json module makes it simple to handle this process.

'''

'''
-----------------------------------------------------------------------------
        Example that will show how to store and read data in or from json files
-----------------------------------------------------------------------------
'''
import json
#creating a dictionary "portfolio" that stores some key-value
portfolio = {
    "name": "rajiv",
    "age" : "19",
    "Nationality" : "Nepalese"
}

#opening a .json file to write data of dictionary(portfolio) into it.
with open("data.json", "w") as file:
    json.dump(portfolio, file)      #this means data of portfolio from file is dumped into json file

with open("data.json", "r") as file:
    dataCarrier = json.load(file)
    print(dataCarrier["age"])