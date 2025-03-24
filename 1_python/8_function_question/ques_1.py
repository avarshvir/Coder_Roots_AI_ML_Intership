"""Question 1: 
Ask user to input a number and show all even number upto that number starting from number 1
Ex: 15
2 4 6 8 10 12 14
"""
number = int(input("Enter number: "))

for i in range(1,number+1):
    if i % 2 == 0:
        print(i,end=" ")

print()

# using user defined function

def evenRange(num):
    for i in range(1,num+1):
        if i % 2 == 0:
            print(i,end=" ")

number_range = int(input("Enter number: "))
evenRange(number_range)

print()
# third method
even_list = set()

def even_list_range(number_range):
    for i in range(1, number_range+1):
        if i % 2 == 0:
            even_list.add(i)
    return even_list

print(even_list_range(number_range),end=" ")

print()

# 4th method
even_list1 = []

def even_list_range(number_range):
    for i in range(1, number_range+1):
        if i % 2 == 0:
            even_list1.append(i)
    return even_list1

print(even_list_range(number_range),end=" ")
    
