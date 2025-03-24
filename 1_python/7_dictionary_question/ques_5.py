# Q5. Write a program that checks the strength of a password based on the following criteria:
# At least 8 characters long
# Contains both uppercase and lowercase characters
# Contains at least one digit
# Contains at least one special character (e.g., !, @, #, $, etc.)

password_in = input("Enter Password: ")

if len(password_in)>= 8 and not(password_in.lower() == password_in):
    print("aditya")

"""
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: At least 8 characters long"
    
    has_lower = has_upper = has_digit = has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_lower:
        return "Weak: No lowercase characters"
    if not has_upper:
        return "Weak: No uppercase characters"
    if not has_digit:
        return "Weak: No digits"
    if not has_special:
        return "Weak: No special characters"
    
    return "Strong password"

password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
"""