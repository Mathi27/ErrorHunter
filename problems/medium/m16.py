# Program to Generate a Random Password
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

length = int(input("Enter password length: "))
if length < 4:
    print("Password length must be at least 4 characters.")
else:
    print("Generated Password:", generate_password(length))
