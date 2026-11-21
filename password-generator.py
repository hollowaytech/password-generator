# @hollowaytech on GitHub
# SECURE PASSWORD GENERATOR (For when you don't feel like thinking of one! :))
# Code to exit program is 101010

# Libraries imported
import string
import secrets
import time
# Password generator function
def generator(length):
    password = ""
    # Exception raising if length doesn't meet requirements (invalid value or limit)
    if length <= 0 or length > 100 and length != 101010:
        raise ValueError
    # Secret exit code
    elif length == 101010:
        print("\nExiting script", end="")
        for i in range(0, 3):
                print(".", end="")
                time.sleep(1)
        exit(0)
    else:
        try:
            print("\nGenerating", end="")
            for i in range(0, 3):
                print(".", end="")
                time.sleep(1)
            for i in range(0,length):
                    password += secrets.choice(string.ascii_letters+string.digits+string.punctuation)
        except ValueError:
            exit(1)
        return password
while True:
    length = int(input("Enter password length >>> ")) # Length is equal to desired character length of password
    password = generator(length)
    print("\n")
    for j in range (0, length+20):
        print("=", end="")
    print(f"\nGenerated password: {password}")
    for j in range (0, length+20):
        print("=", end="")
    print("\n")