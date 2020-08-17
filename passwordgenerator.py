import sys
import string
import secrets


def user_input():
    '''Ask user to enter the length of password they want'''

    # If user called the program from command shell with an argument
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])

        except ValueError:
            sys.exit('Error: You need to pass an integer as argument!')

    # If user did not call the program from command shell with an argument
    while True:
        try:
            passlength = int(input('How many characters do you want in your password? '))
            return passlength

        except ValueError:
            print('\nPlease input an integer\n')


def main():
    '''Generating password as per given length by user'''

    chars = string.printable[:94]
    passlength = user_input()

    password = ''.join(secrets.choice(chars) for _ in range(passlength))
    print(password)


if __name__ == '__main__':
    main()
