"""Given numbers = range(20), produce a list containing the word ‘even’ 
if a number in the numbers is even, 
and the word ‘odd’ if the number is odd. 
Result would look like ‘odd’,'even',........"""

numbers = range(20)
odd_even_number = ['even' if i % 2 == 0 else 'odd' for i in numbers]
print(odd_even_number)
print(len(odd_even_number))