"""create a list of 10 elements and print all elements are even
locations
Example:
    x = [1,4,2,42,4,6,2,56,4,56,2]
    Result is: 1 2 4 6 56 56"""

x = [1,4,2,42,4,6,2,56,4,56,2]
print("First Soution")
print(x[0:11:2])

print("Second Solution")
# print (x)
# print(len(x))
for i in range(len(x)):
    if i % 2 == 0:
        print(x[i])

print("third solution")
index = 0
for i in x:
    if index % 2==0:
        print(i)
    index += 1
