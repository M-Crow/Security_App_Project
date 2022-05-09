# Monoalphabetic Substitution Cipher
from multiprocessing.sharedctypes import Value
import string
import random
import pyfiglet
import time 

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

print(pyfiglet.figlet_format("Hello, Welcome to the Scrambler 5000"))
time.sleep(1)

def main_chiper():
    encrypt_msg = input("Do you want to Encrypt(1) or Decrypt?(2): " )
    if encrypt_msg == "1":
        print(encrypt_chiper())
    elif encrypt_msg == "2":
        print(decrypt_chiper())
    else:
        print("You did not select a valid option")
        main_chiper()

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

main_chiper()





