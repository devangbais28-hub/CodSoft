# Random Password Generator

import random
import string

class PasswordGenerator:
    
    def generate_password(self, length):

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""
        for i in range(length):
            password += random.choice(characters)

        return password


pg = PasswordGenerator()
print("!! PASSWORD GENERATOR !!")

length = int(input("Enter password length: "))
password = pg.generate_password(length)

print("Generated Password:", password)