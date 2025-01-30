"""Question 6:
Write a Python program  take keys and value from user to create a dictionary.

output
enter key =a
value= 12
enter key =b
value= 16
{'a':12 ,b:'16'}
"""

n = int(input("Enter number of time you want to insert key-pair values: "))

my_dict = {}

for i in range(n):
    key_in = input("Enter key: ")
    value_in = input("Enter value: ")
    my_dict[key_in] = value_in
print(my_dict)




