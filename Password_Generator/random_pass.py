# Random Password Generator
import string, random

letter_list = list(string.ascii_letters)
number_list = list(string.digits)
charecter_list = ["!", "@", "#", "$", "%", "^", "&", "*"]

def random_password():
    
    password = ""
    
    password_length = int(input("How long would you like your password to be? Please enter a number 1-20: "))
    
    if password_length > int(20) or password_length < int(1):
        print("You did not enter a valid number")
        password_length = int(input("Please enter a new number: "))
    
    for i in range(password_length):
        password += random.choice(letter_list + number_list + charecter_list)
    return "Your password is: " + password

print(random_password())