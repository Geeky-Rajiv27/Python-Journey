'''
NOTE :      Format methods are the traditional methods for formatiing strings in python
            (before f string feature in python)

            syntax :

          a =  template.format("string1_as argument1", "string2_as arguement2")
                print(a)
'''

#example : 

'''
NOTE: by default the str1 will choose first {} and str2 will choose second {}
'''

FormattedString = "{} is a {} man".format("Rajiv", "good and smart")
print(FormattedString)


'''
NOTE : we can also fix the position of the str1, str2 in a following ways
'''


FormattedString = "{1} is a {0} man".format("Rajiv", "good and smart")
print(FormattedString) #--> output : good and smart is a Rajiv man
