import random

'''Generating characters'''

all_chars = ''

# Range of Unicode characters
start_unicode = 33  # Starting Unicode for characters
end_unicode = 127  # Ending Unicode for characters

# Generating characters
for unicode_val in range(start_unicode, end_unicode + 1):
    char = chr(unicode_val)  # char() converts Unicode number to actual character
    all_chars += char


def gen_password(chars, how_long):
    password = ''
    max_range = len(chars)

    while how_long:
        password += chars[random.randint(0, max_range - 1)]
        how_long -= 1
    return password


quantity = int(input('How many passwords do you want? '))
quality = int(input('How many characters you want in your password(s)? '))
while quantity:
    print(gen_password(all_chars, quality))
    quantity -= 1
