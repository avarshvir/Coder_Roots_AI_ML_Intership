#Question 3:
"""Using User input ask user to input 2 string and tell followings
    1. using == tell both string equal or not
    2. using is operator tell both equal or not"""

str_1 = input("Enter 1st String: ")
str_2 = input("Enter 2nd String: ")

#using == operator
if str_1 == str_2:
    print("Both Strings are equal")
else:
    print("Both Strings are not equal")

#using is operator
if str_1 is str_2:
    print("Both Strings are equal")
else:
    print("Both Strings are not equal")
