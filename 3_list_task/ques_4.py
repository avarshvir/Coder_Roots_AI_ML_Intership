"""Q4. create a list with values ["Gaurav",12,23,33.33,"Sharma",True]
and print only elements which are string"""

my_list = ["Gaurav",12,23,33.33,"Sharma",True]

string_values = [i for i in my_list if type(i) == str]
print(string_values)

# alternative method
"""my_list2 = []
for i in my_list:
    if type(i) == str:
        my_list2.append(i)
print(my_list2)"""