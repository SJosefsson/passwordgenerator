#!/usr/bin/env python3

from passwordgenerator import passwordgenerator


def ask_for_password_size() -> int:
    while True:
        try:
            size = int(input('Password length? '))
        except ValueError as error:
            print('Integer values only. Try again.')
        else:
            return size


def main():
    size = ask_for_password_size()
    password = passwordgenerator.generate_password(size=size)
    print(f'Password generated: {password}')


if __name__ == '__main__':
    main()
