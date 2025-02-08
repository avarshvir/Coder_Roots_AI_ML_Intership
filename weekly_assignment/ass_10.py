"""Write a program that calculates the Body Mass Index (BMI) and 
categorizes it based on the following criteria:
BMI < 18.5: Underweight
18.5 <= BMI < 24.9: Normal weight
25 <= BMI < 29.9: Overweight
BMI >= 30: Obesity"""

bmi_input = float(input("Enter BMI: "))
if bmi_input < 18.5:
    print("Underweight")
elif bmi_input >= 18.5 and bmi_input < 24.9:
    print("Normal weight")
elif bmi_input >= 25 and bmi_input < 29.9:
    print("Overweight")
else:
    print("Obesity")