import random

rps_choice = ['r','p','s']
print(rps_choice)
user_choice = input("Enter choice: ")

comp_choice = random.choice(rps_choice)
print("computer choose ",comp_choice)

if user_choice == comp_choice:
    print("its tie")
elif (user_choice =='r' and comp_choice =='s') or\
     (user_choice == 'p' and comp_choice == 'r') or\
     (user_choice == 's' and comp_choice == 'p'):
    print("user win")
else:
    print("computer wins")