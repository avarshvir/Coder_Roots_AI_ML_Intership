"""Question 2:
WAP Create a list of 10 elements (Number elements) and perform the following
a. Tell element 25 exist or not
b. Total length of List
c. total occurrence of 25 in the list
d. traverse of Each element
e. Show All Even number in list"""

my_list = [1,2,3,4,25,25,8,5,25,10]

number_found = False

for i in my_list:
    if i == 25:
        print("number 25 is exist")
        number_found = True
        break
if not number_found:
    print("number not exist")
    

"""exist_or_not = ["exist 25" if i == 25 else "not exist" for i in my_list ]
print(exist_or_not)"""

print("length of my_list is",len(my_list))

num_list_count = []
for i in my_list:
    if i == 25:
        num_list_count.append(i)

print("Number of 25 occurence: ",len(num_list_count))


print("Traversing of each element")
print(my_list)

print("Traversing of each element using for loop")
for i in my_list:
    print(i,end=" ")

print()

print("Even number in my list: ")
for i in my_list:
    if i % 2 == 0:
        print(i,end=" ")

print()

even_list = []
print("Even number in my list using empty list: ")
for i in my_list:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)
