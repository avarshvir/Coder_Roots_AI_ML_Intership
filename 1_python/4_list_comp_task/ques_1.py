# Find all of the words in a string that are less than 4 letters

input_string = input("Enter String: ")

word = input_string.split()

short_word = [i for i in word if len(i) < 4]
print(short_word)