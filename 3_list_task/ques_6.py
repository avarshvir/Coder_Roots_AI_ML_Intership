"""Q6. Create a list with 5 friends and ask user a friend name and
add that name in the friend list,
and print the list
after that ask user to most important friend and add that friend
at user choice

Ex: [1,2,3,4,5]
-> Enter anothe fiend: Raju
[1,2,3,4,5,"Raju"]
--> Most import afiedn: Billa
--> Please location for billa: 1
[1,"Billa",3,4,5,"Raju"]"""

my_list = ['abc','xyz','qwe','rty','jkl']
print(my_list)
friend_input = input("Enter friend name: ")
my_list.append(friend_input)
print(my_list)

another_friend = input("Enter most important friend: ")
location_input = int(input("Enter location: "))

my_list[location_input] = another_friend

print(my_list)

