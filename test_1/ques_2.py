"""2. Create a dictionary of 10 items as below{a:10,b:20,c:30,d:50,f:10,g:40,k:10,l:30,m:34,z:33}

print the following
1. All items
2. Sum of All Items values
3. Average of all items
Optionals
4. Max in All items
5. min in all items
6. Max occur item"""

dict1 = {
    'a':10,
    'b':20,
    'c':30,
    'd':50,
    'f':10,
    'g':40,
    'k':10,
    'l':30,
    'm':34,
    'z':33}


print("--------------------------")
print(dict1)

print("..........................")
for i in dict1.items():
    print(i)

print("---------------------------")
sum = 0
for i in dict1.values():
    sum = i+sum
print(sum)

print("---------------------------")
print(sum/len(dict1.values()))

print("----------------------------")
maximum = 0
for i in dict1.values():
    if i > maximum:
        maximum = i
print(maximum)

print("-----------------------------")
minimum = maximum  #float('inf')
for i in dict1.values():
    if i < minimum:
        minimum = i
print(minimum)

#print(min(dict1.values()))

print("------------------------------")


    