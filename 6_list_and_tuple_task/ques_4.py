#Create a list of tuples using list comprehension, 
#where each tuple contains a number and its cube for numbers from 1 to 5.

cubes = [(num, num**3) for num in range(1, 6)]
print(cubes)
