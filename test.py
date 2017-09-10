import hashlib, binascii
import random

def make_salt():

    characters = []
    SALT_LENTH = 5

    for char in range(SALT_LENTH):
        characters.append(random.choice('abcdefghijk'))

    return ''.join(characters)


def make_pw_hash(pw, salt=None):

    if not salt:
        salt = make_salt()
    hash_byte = hashlib.pbkdf2_hmac('sha256', pw.encode('utf-8'), salt.encode('utf-8'), 100000)
    hash_str = binascii.hexlify(hash_byte).decode()

    return ','.join([hash_str, salt])

name = 'Alexey'
pw = '123'
hash = 'c519464c0e4f3a7310b8d4eb40a1f6956f03edca455a014247da29c3bc873548,gikac'

def valid_pw(name, pw, hash):

    _, salt = hash.split(',')
    hash_for_compare = make_pw_hash(pw, salt)

    return hash_for_compare == hash

print(valid_pw(name, pw, hash))
#       отрезать соль из хэша
#       передать в make_pw_hash
#       захэшировать с полученной солью
