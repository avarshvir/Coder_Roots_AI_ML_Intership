# Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, 
# and the user tries to guess it. The program should give hints if the guess is too high or too low.

import random

user_input = int(input("Enter the Number: "))

computer_guess = random.randint(1,100)

print("Computer guess the number is: ",computer_guess)

if user_input == computer_guess:
    print("numbers are same")
elif computer_guess >= user_input:
    print("number is too high that is guess by computer") 
else:
    print("number is too low that is guess by computer") 
