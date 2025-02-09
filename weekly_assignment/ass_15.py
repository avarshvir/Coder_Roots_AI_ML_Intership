# Write a program to count the number of vowels in a given string

string_in = input("Enter String: ")

vowel = ['a','e','i','o','u']

count = 0
for char in string_in:
    if char.lower() in vowel:
        count +=1
        print(char)

print(f"No. of Vowels in {string_in} is : {count}")