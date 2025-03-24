#/Q1 Take a empty Dictionary and Ask user to input the number of time they want to enter and 
# input form user to make dict


my_dict = {}

num = int(input("How many key-value pairs do you want to add? "))

for i in range(num):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value 

print("Final Dictionary:", my_dict)