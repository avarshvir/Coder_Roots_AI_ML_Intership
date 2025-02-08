"""Write a program that takes an integer input representing a 
day of the week (1 for Monday, 2 for Tuesday, etc.)
and prints the corresponding day name."""

days = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}

day_in = int(input("Enter No: "))

print(days.get(day_in))

