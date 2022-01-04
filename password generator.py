#generate your own password

digits = '123456789' #choose as many digits as you want
chars = 'abcdefghijklmn' \
    'opqrstuvwxyz'
up = chars.upper()
special = '_!$%&?'
all = digits+chars+up+special
from random import choice
password = ''.join(
    choice(all) for i in range(8)
)

print(password)