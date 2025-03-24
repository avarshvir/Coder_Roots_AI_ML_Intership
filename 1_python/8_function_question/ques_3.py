"""Question 3:
Ask User to input a String of min 10 words and max 19 words and perform the following:
1. Print full string and length of string
2. Tell String is palindrome or not mean
3. Tell middle word in the string.
4. Print Second last word in the String."""

def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter the String of min 10 words and max 19 words: ")

if len(input_string) >= 10 and len(input_string) <= 19:

    #1
    print(input_string)
    print("length of string is: ",len(input_string))

    #2
    if is_palindrome(input_string.replace(" ", "").lower()):
        print("The string is a palindrome.")
    else:
        print("The string is NOT a palindrome.")

    #3
    mid_index = len(input_string) // 2
    print("Middle word:", input_string[mid_index])

    #4
    print("Second Last word: ", input_string[-2] )

else:
    print("Please Enter the String of min 10 words and max 19 words!")