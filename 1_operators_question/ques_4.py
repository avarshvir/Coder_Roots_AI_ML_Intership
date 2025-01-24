"""Write a program to:
Take the temperature in Celsius as input (string format).
Convert it into a float.
Calculate the equivalent temperature in Fahrenheit using the formula: Fahrenheit=(Celsius×59​)+32
Print the result in both Celsius and Fahrenheit."""

celsius_temperature = input("Enter the temperature")
celsius = float(celsius_temperature)
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Celsius:",celsius, "C")
print(f"Temperature in Fahrenheit:",fahrenheit,"F")
