# Find all of the numbers from 1-1000 that are divisible by 7

numbers = range(1,1000)
divisible_by_7 = [i for i in numbers if i % 7 == 0]
print(divisible_by_7)