# Write a program to find the sum of the first n natural numbers.

nat_num = int(input("Enter the range: "))

sum = 0

for i in range(1, nat_num+1):
    sum+= i
print(sum)