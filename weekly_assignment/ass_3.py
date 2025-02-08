# Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. 
# The grading scheme is:
"""90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F"""

user_in = int(input("Enter Score Between 0 and 100: "))

if user_in >= 90 and user_in <= 100:
    print("A")
elif user_in >= 80 and user_in <= 89:
    print("B")
elif user_in >= 70 and user_in <= 79:
    print("C")
elif user_in >= 60 and user_in <= 69:
    print("D")
else:
    print("F")

