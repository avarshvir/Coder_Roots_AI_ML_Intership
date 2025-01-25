"""7.  Ask User to input a Number and with + or - and perform followingsOutput
   Enter a no: 567
   Enter OP(+,-): +
   0,1,2,3.......566
   if -
   567...>..... 1"""

num = int(input("Enter a number: "))
op = input("Enter OP(+,-)")

if op == '+':
    for i in range(0,num):
        print(i,end=" ")
elif op == '-':
    for i in range(num,0,-1):
        print(i,end=" ")