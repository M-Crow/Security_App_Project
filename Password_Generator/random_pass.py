# Random Password Generator
import string, random

letter_list = list(string.ascii_letters)
number_list = list(string.digits)
charecter_list = ["!", "@", "#", "$", "%", "^", "&", "*"]

def random_password():
    random_pass = ""
    user_input = int(input("How long would you like your password to be? Please enter a number 1-20: "))
    if user_input > int(20) or user_input < int(1):
        print("You did not enter a valid number")
        user_input = int(input("Please enter a new number: "))
    for i in range(user_input):
        random_pass += random.choice(letter_list + number_list + charecter_list)
    return "Your password is: " + random_pass

print(random_password())