"""Write a Python program to get a single string from two given strings, separated by a space and 
swap the first characters of each string
Sample String : 'coder', 'roots'
Expected Result : 'roder coots' """

str_1 = input("Enter 1st String: ")
str_2 = input("Enter 2nd String: ")

a = str_2[0]+str_1[1:]
b = str_1[0]+str_2[1:]

print(a," ",b)