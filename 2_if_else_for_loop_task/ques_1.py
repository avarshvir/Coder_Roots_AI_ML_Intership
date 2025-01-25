#Question 1
"""WAP Ask user to input a number and then
month name corresponding to that number"""

month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

mon_num = int(input("Enter month number :"))

if mon_num == 1:
    print("jan")
elif mon_num == 2:
    print("feb")
elif mon_num == 3:
    print("mar")
elif mon_num == 4:
    print("apr")
elif mon_num == 5:
    print("may")
elif mon_num == 6:
    print("jun")
elif mon_num == 7:
    print("jul")
elif mon_num == 8:
    print("aug")
elif mon_num == 9:
    print("sep")
elif mon_num == 10:
    print("oct")
elif mon_num == 11:
    print("nov")
elif mon_num == 12:
    print("dec")
else:
    print("invalid month number")
