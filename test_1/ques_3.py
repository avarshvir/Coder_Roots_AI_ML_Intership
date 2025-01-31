"""3. Create a list with 5 friends and ask user a friend name andadd that name in the friend list,
and print the list
after that ask user to most important friend and add that friend
at user choice

Ex: [1,2,3,4,5]
-> Enter anothe fiend: Raju
[1,2,3,4,5,"Raju"]
--> Most import afiedn: Billa
--> Please location for billa: 1
[1,"Billa",3,4,5,"Raju"]"""

friend_list = [1,2,3,4,5]
another_friend = input("Enter another friend: ")
friend_list.append(another_friend)
print(friend_list)


imp_friend = input("most important friend: ")
print("location for friend: ",imp_friend,": ",end="")
friend_loc = int(input())

friend_list[friend_loc] = imp_friend

print(friend_list)

"""for i in friend_list:
    if i == friend_list:
        i[]"""

