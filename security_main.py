# Main hub for security app

from multiprocessing.sharedctypes import Value
import string, random, pyfiglet, time

print(pyfiglet.figlet_format("Welcome to your Security Hub"))

def main_screen_selection():
        selection = input("Please select and option to continue: (1) for Encryption, (2) for a random password ")
        if selection == "1":
            print("You will now be redirected to the Encryption program")
            print(encryption_cipher())
        elif selection == "2":
            print("You will now be redirected to the Random Password program")
            print(random_password_generator())

def encryption_cipher():

    alpha = {
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
        'n': 'm',
        'o': 'l',
        'p': 'k',
        'q': 'j',
        'r': 'i',
        's': 'h',
        't': 'g',
        'u': 'f',
        'v': 'e',
        'w': 'd',
        'x': 'c',
        'y': 'b',
        'z': 'a',
        ' ': ' ',
    }
    inverse_alpha = {v:k for k, v in alpha.items()}
    encrypted_message = []

    print("Welcome to the Encryption/Decryption program!")

    def main_call_chiper():
        encrypt_msg = input("Do you want to Encrypt(1) or Decrypt?(2): " )
        if encrypt_msg == "1":
            print(encrypt_chiper())
        elif encrypt_msg == "2":
            print(decrypt_chiper())
        else:
            print("You did not select a valid option")
            main_call_chiper()

    def encrypt_chiper():
        message = input("Enter message: ")
        message = message.lower()
        while message.isdigit():
            print("No numbers allowed")
            new_message = input("Please enter another message: ")
            if new_message.isalpha():
                message = new_message
        for letter in message:    
            encrypted_message.append(alpha.get(letter, letter))
        return ''.join(encrypted_message)

    def decrypt_chiper():
        message_decrypt = encrypt_chiper()
        print("The encrypted message is: " + ''.join(message_decrypt))
        decrypt_message = []
        for letter in message_decrypt:
            decrypt_message.append(inverse_alpha.get(letter, letter))
        return "The decrypted message is: " + ''.join(decrypt_message)

    main_call_chiper()

def random_password_generator():
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
        while password_length > int(20) or password_length < int(1):
            print("You did not enter a valid number")
            password_length = int(input("Please enter a new number: "))
        if password_length > int(20) or password_length < int(1):
            return password_length
        
        # Randomly generates a password of x length. X is equal to the password_lenght the user provided
        for i in range(password_length):
            password += random.choice(letter_list + number_list + charecter_list)
        return "Your password is: " + password

    # Calls the function to generate a random password 
    print(random_password())

main_screen_selection()