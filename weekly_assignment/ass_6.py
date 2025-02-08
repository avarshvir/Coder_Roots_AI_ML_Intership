# Write a program to check if a given year is a leap year. 
# A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

given_year = int(input("Enter the year: "))

if (given_year % 4 == 0 and given_year % 100 != 0) or given_year % 400 == 0:
    print(f"{given_year} Year is a Leap Year")
else:
    print(f"{given_year} Year is not a Leap Year")