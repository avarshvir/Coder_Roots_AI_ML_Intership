# Write a program that prints the multiplication table (from 1 to 10) for a given number

table = int(input("Enter 1 to 10 to print the table: "))

if table >=1 and table <= 10:
    for i in range(1,11):
        result = table * i
        print(f"{table} X {i} = {result}")
else:
    print("Please enter 1 to 10")