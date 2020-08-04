import string
import secrets
import sys

def main():
    # Creating a list of all the characters that can be used when
    # generating the password
    chars = list(string.ascii_letters + string.digits + string.punctuation)

    # Call password_creation with chars and user_input as arguments
    password_creation(chars, user_input())

def user_input():
    # If user called the program from command shell with an argument
    # Check if argument is valid (int), and return it
    # If argument is not valid exit program with an error.
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            sys.exit('Error: You need to pass an integer as argument!')

    # If user did not call the program from command shell with an argument
    # Ask user how long they want their password to be
    while True:
        try:
            passlength = int(input(
                'How many characters do you want in your password? '))
            break
        except ValueError:
            print('Please input an integer')
    return passlength

def password_creation(chars, passlength):
    # Creating the password
    password = ''.join(secrets.choice(chars) for _ in range(passlength))

    # Printing password so it can be copied
    print(password)

if __name__ == '__main__':
    main()