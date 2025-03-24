"""Write a python program that takes in a student name, class, and section. 
It should also take in five subject marks of the students and find the total mark and percentage. 
Display a result in such a way that their name, class, section, and percentage are printed."""

s_name = input("Enter Student Name: ")
s_class = input("Enter Student Class: ")
s_section = input("Enter Student Section: ")

sub_1 = float(input("Enter marks of subject 1: "))
sub_2 = float(input("Enter marks of subject 2: "))
sub_3 = float(input("Enter marks of subject 3: "))
sub_4 = float(input("Enter marks of subject 4: "))
sub_5 = float(input("Enter marks of subject 5: "))

total_marks = sub_1+sub_2+sub_3+sub_4+sub_5
percentage = (total_marks/500)*100

print("------- Student Result -------")
print(f"Name: ", s_name)
print(f"Class: ", s_class)
print(f"Section: ", s_section)
print(f"Total Marks: ", total_marks)
print(f"Percentage: ", percentage, "%")

