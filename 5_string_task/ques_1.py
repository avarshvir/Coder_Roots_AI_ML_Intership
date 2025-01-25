"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return ‘not a valid string’ instead of the empty string
Sample string: - “Coder roots”
Expected result - “cots”
Sample string - “New year”
Expected result - “near” """

str_1 = input("Enter 1st String: ")

if len(str_1) < 2:
    print("not a valid string")
else:
    a = str_1[:2]
    b = str_1[-2:]
    if str_1.capitalize():
        print(a.lower()+b.lower())