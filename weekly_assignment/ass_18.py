# Write a program for a number guessing game where the computer randomly 
# selects a number between 1 and 100, and the user tries to guess it. 
# The program should give hints if the guess is too high or too low.

import random

comp_choice = random.choice(range(1,100))

user_choice = int(input("Enter number: "))

if user_choice > 100 or user_choice < 0:
    print("please enter number between 0 to 100")
    exit(0)

if user_choice == comp_choice:
    print("Same Number")
elif user_choice > comp_choice:
    print("user choose is too high")
else:
    print("user choice is too low")
    
    

print("Computer Chooses: ",comp_choice)

