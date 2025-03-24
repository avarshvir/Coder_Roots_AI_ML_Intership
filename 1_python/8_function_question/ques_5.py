"""Question 5:
Write a Python program to count the number of strings where the
string length is 2 or more and the first and last character are same
from a given list of strings.

Input :

X = ['abc', 'xyz', 'aba', '1221']

Output :

2"""

X = ['abc', 'xyz', 'aba', '1221']
#print(X)

def count_strings(a):
    count = 0
    for i in a:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

print(count_strings(X))
