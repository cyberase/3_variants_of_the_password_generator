import random

def generatePassword(length):
    characters = [chr(n) for n in range(33, 127)]
    return "".join(random.choices(characters, k=length))

length = int(input("Enter your password length: "))
print(length)
print(generatePassword(length))