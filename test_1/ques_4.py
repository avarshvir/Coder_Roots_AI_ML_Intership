"""4.Write a program to check if a given year is a leap year. A year is a leap year 
if it is divisible by 4, but not by 100, unless it is also divisible by 400."""

year_in = int(input("Enter year: "))

if (year_in % 4 == 0 and year_in % 100 != 0) or (year_in % 400 == 0):
    print(year_in, "is a Leap Year")
else:
    print(year_in, "is NOT a Leap Year")