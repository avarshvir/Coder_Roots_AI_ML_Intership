import random

print("-------------------------------------")
print("Welcome to Rock Paper Scissor Game :)")
print("Before we Start we need some user info: ")
print("Are you agree with our T&C. yes/no")

user_score = 0
comp_score = 0

t_c = input()
if t_c == 'yes':
    name_input = input("Enter your Name: ")
else:
    print("Soon we will meet :)")
    exit(0)
print("---------------------------------------")

rps_choice = ['r','p','s']
print("Rock - r \nPaper - p \nScissor - s")

def get_user_choice():
    user_choice = input("Enter choice: ")
    print(f"{name_input} Chooses: ", user_choice)
    return user_choice

def get_comp_choice():
    comp_choice = random.choice(rps_choice)
    print("Computer Chooses: ", comp_choice)
    return comp_choice 

def winner(user,comp):
    global user_score
    global comp_score
    if user == comp:
        print("its tie")
        #score = score + 0
    elif (user =='r' and comp =='s') or\
         (user == 'p' and comp == 'r') or\
         (user == 's' and comp == 'p'):
        print(f"{name_input} win")
        user_score += 1
    else:
        print("computer wins")
        comp_score += 1


while True:
    user = get_user_choice();
    comp = get_comp_choice();
    winner(user,comp)
    with open('r_p_c_file.txt','w') as rps:
        rps.write(f"Current {name_input} Score: {user_score}\n")
        rps.write(f"Current Computer Score: {comp_score}\n")
        #rps.close()
        

    print(f"Current {name_input} Score: {user_score}")
    print(f"Current Computer Score: ", comp_score)
    print(f"{name_input} do you want yo play again. yes or no.")
    play_again = input()
    #print(score)
    if play_again != 'yes':
        print("Thanks for Playing :)")
        exit(0)
    