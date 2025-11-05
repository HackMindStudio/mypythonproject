import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

while True:
    user_input = input("Enter password length (0 or 'exit' to quit): ")
    if user_input.lower() == "exit" or user_input == "0":
        print("Exiting...")
        break
    try:
        length = int(user_input)
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a number or type 'exit' to quit.")
