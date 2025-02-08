# Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.

int_input = int(input("Enter Integer: "))


if int_input > 0:
    print(f"{int_input} is a Positive number.")
elif int_input == 0:
    print(f"{int_input} is a Zero.")
else:
    print(f"{int_input} is a Negative number.")