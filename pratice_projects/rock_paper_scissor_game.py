import random

print("Welcome to Rock Paper Scissor Game :)")
user_name = input("Enter your Name: ")


rps_choice = ['r','p','s']

def get_user_choice():
    print(rps_choice)
    user_choice = input("Enter the choice: ").lower()
    print(user_name,f" chooses {user_choice}")
    return user_choice
    

def get_comp_choice():
    comp_choice = random.choice(rps_choice)
    print("computer chooses ",comp_choice)
    return comp_choice

def winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return f"{user_name} wins!"
    else:
        return "Computer wins!"
    

while True:
    user_choice = get_user_choice()  
    comp_choice = get_comp_choice()  
    print(winner(user_choice, comp_choice))  
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break


    
