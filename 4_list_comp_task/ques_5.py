"""Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5"""

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_list = [i for i in list_a if i in list_b]
print(common_list)


"""common_list = []

for i in list_a:
    for j in list_b:
        if i == j:
            common_list.append(i)
print(common_list)"""
