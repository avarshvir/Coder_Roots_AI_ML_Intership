# Write a program to print all prime numbers between 1 and 100

n = range(2,100)

for i in n:
    if n % i == 0:
        break
    else:
        print(i,end=" ")
    