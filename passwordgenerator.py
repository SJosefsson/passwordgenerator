import string, random

map = list(string.ascii_letters)
map.append('-')
map.append('_')
map.extend(range(10))

passlength = int(input('How many characters do you want in your password? '))
password = ''

while len(password) < passlength: password += str(map[random.randint(0, len(map) - 1)])

print(password)