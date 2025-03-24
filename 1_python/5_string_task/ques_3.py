"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly' """

str_1 = input("Enter string: ")

if len(str_1) < 3:
    print(str_1)
elif str_1.endswith("ing"):
    print(str_1+"ly")
else:
    print(str_1+"ing")
