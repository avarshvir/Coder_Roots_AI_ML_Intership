"""5.Write a program that takes the lengths of three sides of a triangle as input and 
determines the type of triangle (equilateral, isosceles, or scalene, right angle traingle)"""


def triangle_determination(a,b,c):
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Right Angle Triangle")

len1 = int(input("Enter 1st side: "))
len2 = int(input("Enter 2nd side: "))
len3 = int(input("Enter 3rd side: "))

triangle_determination(len1,len2,len3)