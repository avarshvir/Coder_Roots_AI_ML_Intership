#Question 4:
"""ask user to input 2 string and convert it into numbers and using is op
    tell both are euqal or not"""

str_1 = input("Enter 1st String: ")
str_2 = input("Enter 2nd String: ")

num_1 = int(str_1)
num_2 = int(str_2)

if num_1 is num_2:
    print("Both are equal")
else:
    print("Not Equal")
 