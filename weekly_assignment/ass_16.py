#16. Write a program to find the sum of the digits of a given number.

num = int(input("Enter the number: "))

if num < 0:
    num = -num

sum = 0

while num > 0:
    remaining = num % 10
    sum += remaining
    num //=  10

print(sum) 