import random
def get_random_code(length):
"""
Generates a random string of letters and digits of given length

:param length: Desired length of string
:type length: int
:return: Random string
:rtype: str
"""
letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
password = ''
for i in range(length):
    password += random.choice(letters + digits)
return password