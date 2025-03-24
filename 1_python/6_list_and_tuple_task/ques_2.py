"""Write a list comprehension to flatten a 2D list into a 1D list
                        Input: [[1, 2], [3, 4], [5, 6]] → Output: [1, 2, 3, 4, 5, 6]"""

flatten_list = [item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]
print(flatten_list)