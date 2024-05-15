import re

def check_password_strength(password):
   
    length_criteria = 8
    uppercase_criteria = True
    lowercase_criteria = True
    digit_criteria = True
    special_char_criteria = True
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
   
    if len(password) < length_criteria:
        return "Weak: Password must be at least {} characters long.".format(length_criteria)

    if uppercase_criteria and not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    if lowercase_criteria and not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."


    if digit_criteria and not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    if special_char_criteria and not any(char in special_characters for char in password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Password meets all criteria."

password = input("Enter your password: ")
print(check_password_strength(password))
