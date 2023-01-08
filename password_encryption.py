import hashlib
import os
import base64


def password_hash(password):
    password = input('Enter your password: ')

    # Salt the PW using a randomly generated salt
    salt = hashlib.sha256(os.random(60)).hexdigest().encode('ascii')

    # Has the PW using PBKDF2 w/ HMAC and SHA-256
    pbkdf2 = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000)

    # Encode the salt and hashed PW as base64
    hashed_pw = base64.b64encode(salt+pbkdf2)

    with open('hashed_pw.txt', 'w') as f:
        f.write(hashed_pw).decode('utf-8')
