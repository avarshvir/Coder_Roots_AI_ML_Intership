"""Question 4:
Perform the following Task as per the output

Welcome to Calci:
1. Power 
2. Sum
3. Sub
4. Multiple

Enter your choice. --> 2
Enter 1st Number for Sum: 100
Enter 2nd number for SUm: 200
Sum is 300"""

def add(a,b):
    return a+b

def power(a,b):
    return a**b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")


while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(power(2,3))
    elif choice == 2:
        print("The Sum is", add(100,200))
    elif choice == 3:
        print("The difference is", subtract(200,100))
    elif choice == 4:
        print("The multiplication is", multiply(10,10))
    else: 
        print("Invalid Choice")
        #break
    another_input = input("Do you want to continue: ")
    if another_input != 'yes':
        break

