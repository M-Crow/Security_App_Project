# Random Password Generator
import string, random

# List containing all uppercase/lowercase letters, numbers 0-9, and some specical charecters
letter_list = list(string.ascii_letters)
number_list = list(string.digits)
charecter_list = ["!", "@", "#", "$", "%", "^", "&", "*"]

# Function that ask the user for a password length and outputting a random password based on the users-input 
def random_password():
    
    password = ""
    
    # User inputs a number 1-20 to determine the length of their password 
    password_length = int(input("How long would you like your password to be? Please enter a number 1-20: "))
    
    # If the input is above 20, or below 1, the user will have to input another number within range
    if password_length > int(20) or password_length < int(1):
        print("You did not enter a valid number")
        password_length = int(input("Please enter a new number: "))
    
    # Randomly generates a password of x length. X is equal to the password_lenght the user provided
    for i in range(password_length):
        password += random.choice(letter_list + number_list + charecter_list)
    return "Your password is: " + password

# Calls the function to generate a random password 
print(random_password())