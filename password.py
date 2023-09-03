import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "@#$%^&*!"
digits = "0123456789"

Desired_length = int(input("Enter the Desired length of the password: "))

combination_of_characters= lowercase_letters + uppercase_letters + special_characters + digits 
password = ''.join(random.choice(combination_of_characters)for _ in range(Desired_length))

print("Generated Password:", password)
