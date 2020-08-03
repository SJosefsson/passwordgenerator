import string
import secrets
import sys

def main():
    # Creating a list of all the characters that can be used when
    # generating the password
    chars = list(string.ascii_letters + string.digits
    + '-' + '_' + '!' + '?' + '#' + '+' + '=' + '/' + '*' + '^'
    + '£' + '$' + '%' + '&' + '(' + '[' + '{' + ')' + ']' + '}')
    if len(sys.argv) > 1:
        try:
            password_creation(chars, int(sys.argv[1]))
        except ValueError:
            sys.exit('You need to enter a digit as argument!')
    else:
        passlength = user_input()
        password_creation(chars, passlength)

def user_input():
    # Asking user how long they want their password to be
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