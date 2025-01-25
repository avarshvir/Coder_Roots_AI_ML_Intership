# Write a Python program to remove the nth index character from a nonempty string

str_1 = input("Enter String: ")
int_index = int(input("Enter the index number to remove character"))


if not str_1:
    print("nothing remove as string is empty")

else:
    res = str_1[:int_index]+str_1[1+int_index:]
    print(res)
    