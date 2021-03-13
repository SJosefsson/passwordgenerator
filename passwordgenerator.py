import string, random

symbols = list(string.ascii_letters)
symbols.append('-')
symbols.append('_')
symbols.extend(range(10))

passlength = int(input('How many characters do you want in your password? '))
password = ''

while len(password) < passlength: password += str(symbols[random.randint(0, len(symbols) - 1)])

print(password)