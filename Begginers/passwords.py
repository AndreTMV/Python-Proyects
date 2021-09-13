import getpass
import sys
import string
import random


def password_entry():
    # password:
    # Enter password: APassword
    password = getpass.getpass(stream=sys.stderr)
    return password


def good_password(password):
    # If there's no a cappital letter in the string ...
    if not (any(letter.isupper() for letter in password)):
        print("Your password needs at least 1 capital letter")
        return False
    # If the string is not long enough ...
    elif not (len(password) >= 12):
        print("Your password is to short, it needs at least 12 characters")
        return False
    # If there's no a number in the string ...
    elif not(any(number.isdigit() for number in password)):
        print("Your password needs at least a number")
        return False
    else:
        print("Your password:", password)
        return True


def generate_password():
    # Number of characters of the string
    password_lenght = 12
    # call random.choices() string module to find the string in Uppercase + numeric data.
    password = ''.join(random.choices(
        string.ascii_letters + string.digits, k=password_lenght))
    return password


def main():
    generate_random = input("Do you wanna generate a random password? (Y/N): ")
    if generate_random.lower() == 'y' or generate_random.lower() == 'yes':
        password = generate_password()
        print("Your password: ", password)
    else:
        print("Minimum requirements: \nAt least 1 cappital letter \nAt least one digit")
        good_Password = False
        while good_Password != True:
            password = password_entry()
            good_Password = good_password(password)


if __name__ == '__main__':
    main()
