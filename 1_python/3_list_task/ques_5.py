# Q5. add all the number present in above list

my_list = ["Gaurav",12,23,33.33,"Sharma",True]

sum = 0

for i in my_list:
    if type(i) == int or type(i) == float:
        sum+=i
print(sum)
        