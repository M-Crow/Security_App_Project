# Main hub for security app

from multiprocessing.sharedctypes import Value
import string, random, pyfiglet, time

print(pyfiglet.figlet_format("Welcome to your Security Hub"))

def main_screen_selection():
    selection = input("Please select and option to continue: (1) for Encryption, (2) for a random password ")
    if selection == "1":
        print("You will not be redirected to the Encryption program")
    elif selection == "2":
        print("You will now be redirected to the Random Password program")


