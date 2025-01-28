# Write a Python program to find the maximum and minimum elements in a tuple.
# Input: (3, 5, 1, 8, 2) → Output: Max: 8, Min: 1

my_tuple = (3,5,1,8,2)

maximum = my_tuple[0]
minimum = my_tuple[0]

for i in my_tuple:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
print(f"Max: {maximum}, Min: {minimum}")
    