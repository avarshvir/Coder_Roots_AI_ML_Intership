# Question 5.  Python program to calculate the sum of all numbers from 1 to a given number.

given_num = int(input("Enter Number to calculate sum: "))

sum = 0
for i in range(1, given_num+1):
    sum = sum+i
print(sum) 