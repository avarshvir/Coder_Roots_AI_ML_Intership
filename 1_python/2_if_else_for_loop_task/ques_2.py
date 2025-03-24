#Question 2
#WAP Ask user to input 2 number,
#tell the followings
#1. Both number are equal or not
#2. Which is Bigger in both
#3. Either First NUmber is smaller or equal to Second Number
#4. Print your first name 5 times is first number is
#   greather than second and print your surname 3 times if 1st no
#   is less than second

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

if(num_1 == num_2):
    print("Both numbers are equal")
elif(num_1 > num_2):
    print("Number 1 is greater")
    for i in range(5):
        print("Arshvir")
else:
    print("Number 2 is greater")
    for i in range(3):
        print("Naranch")

"""
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

#1st part
if(num_1 == num_2):
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

#2nd part
if(num_1 > num_2):
    print("Number 1 is greater")
else:
    print("Number 2 is greater")

#3rd part
if(num_1 <= num_2):
    print("Number 1 is smaller or equal to Number 2")

#4th part
if(num_1 > num_2):
    for i in range(5):
        print("Arshvir")
else:
    for i in range(3):
        print("Naranch")"""