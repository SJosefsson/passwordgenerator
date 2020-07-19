import random
import string


class PasswordGenerator:
    def __init__(self, password_length):
        self.string = string.printable[:62]   # Getting number, uppercase and lowercase
        self.password_length = password_length

    def generate(self):
        '''Generating random password as per the password_length'''

        try:
            password = ''.join([random.choice(self.string) for _ in range(self.password_length)])
            print(password)

        except ValueError:
            print('Password Length was expected in integers')


if __name__ == '__main__':
    password_generate = PasswordGenerator(10)
    password_generate.generate()
