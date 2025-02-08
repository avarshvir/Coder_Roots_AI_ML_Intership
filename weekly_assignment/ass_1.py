# Write a program that prints the numbers from 1 to 50. 
# For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i,": FizzBuzz")
    elif i % 3 == 0:
        print(i,": Fizz")
    elif i % 5 == 0:
        print(i,":Buzz ")
    else:
        print(i)