"""6.  Ask user to input a number and tell all even number
   upto that number
 Eg:
   input a num:29
   Even are:
   2,4,6,... 28"""

num = int(input("Enter the number: "))
print("Even are:")

for i in range(1,num+1):
    if(i%2==0):
        print(i,end=",")