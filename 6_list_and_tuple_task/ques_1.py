# Given a tuple, write a Python function to remove all duplicate elements and return a new tuple.

input_tuple = (1, 2, 2, 3, 4, 4, 5)

print("Original Tuple:", input_tuple)
remove_duplicates = set(input_tuple)
t = tuple(remove_duplicates)
print("Tuple without Duplicates:", t)