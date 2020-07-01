import string, random

map = list(string.ascii_letters)
map.append('-',)
map.append('_')

passlength = int(input('How many characters do you want in your password? '))
password = ''

while len(password) < passlength: password += map[random.randint(0, 53)]

print(password)