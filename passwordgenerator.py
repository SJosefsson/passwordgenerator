import string
import secrets
import sys


def main():
    '''Generates a password with a length that the user inputs'''
    
    # Creating a list of chars to use when generating the password
    chars = list(string.printable[:94])

    # Creates the password with chars and user_input() as arguments
    print(''.join(secrets.choice(chars) for _ in range(user_input())))


def user_input():
    '''Asks user how long they want their password to be'''

    # If user called the program from command shell with an argument
    # Make sure it's an int or throw an error
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
            return passlength
        except ValueError:
            print('Please input an integer')


if __name__ == '__main__':
    main()