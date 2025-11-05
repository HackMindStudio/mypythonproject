import re

def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength rating
    if strength <= 2:
        return "Weak 🔴"
    elif strength == 3:
        return "Moderate 🟡"
    else:
        return "Strong 🟢"

password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
