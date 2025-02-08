# Write a program to create a list of the squares of the even numbers from 1 to 20.

even_number_square = []

for i in range(1,21):
    if i % 2 == 0:
        even_number_square.append(i**2)

print(even_number_square)

# 2nd method:

even_number_square2 = [x**2 for x in range(2,21,2)]
print(even_number_square2)