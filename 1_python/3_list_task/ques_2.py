"""Create a list [1,10,100,3,6,8] and add 59 on 3 location after
that append 5 and print list and length of list"""

li = [1,10,100,3,6,8]
#print(li)
li.insert(3,59)
li.append(5)

print(li)
print(len(li))