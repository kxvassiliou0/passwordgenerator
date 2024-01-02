import random # Dice roll function
import string # More ability with strings

# Accepts a length of integer 10
def generatePassword(length: int = 10):
    alphabet = string.ascii_letters = string.digits + string.punctuation # Creates a list of all ascii characters available, including digits and symbols
    password = ''.join(random.choice(alphabet) for i in range(length)) # Blank statement, joined with choosing 10 characters at random, creating a new string
    return password
    
password = generatePassword() # Variable representing the output of generatePassword function
print(f'Generate password: {password}')