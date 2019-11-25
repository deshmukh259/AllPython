from uu import encode

from cryptography.fernet import Fernet

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def passwordtokey():
    global key
    password_provided = "morrisonsAuthentication"  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt='salt'.encode(),
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))



def v(k):
    print(k)
    message = k.encode()
    f = Fernet(passwordtokey())
    encrypted = f.encrypt(message)
    print(encrypted)
    print('--------')

    decrypted = f.decrypt(encrypted)
    print('--------')
    print('\n')
    print((decrypted).decode("utf-8"))
    print(decrypted.decode("utf-8")==k)

def enc1(k):
    print(k)
    message = k.encode()
    f = Fernet(passwordtokey())
    encrypted = f.encrypt(message)
    print('********')
    print(encrypted)
    print(encrypted.decode("utf-8"))
    print('--------')

    decrypted = f.decrypt(encrypted)
    print('--------')
    print('\n')
    print((decrypted).decode("utf-8"))
    print(decrypted.decode("utf-8")==k)

def enc1d(k):
    print(k)
    #message = k.encode()
    f = Fernet(passwordtokey())
    #encrypted = f.encrypt(message)
    print('********')
    #print(encrypted)
    #print(encrypted.decode("utf-8"))
    print('--------')
    kk= k.encode()
    print(kk)
    type(kk)
    decrypted = f.decrypt(kk)
    print('--------')
    print('\n')
    print((decrypted).decode("utf-8"))
    print(decrypted.decode("utf-8")==k)

def enc():
    message = "my deep dark secret".encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(encrypted)

def get_decryped_password(key, encrypted_name):
    #encrypted_name = str.encode(encrypted_name)
    password_provided = key  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    f = Fernet(base64.urlsafe_b64encode(kdf.derive(password)))
    #encrypted_name =f.encrypt(str.encode(encrypted_name))
    return f.decrypt(encrypted_name.encode())
    #return f.decrypt(encrypted_name)

def decrypt(data, password):
    """Decrypts data using the password.

    Decrypts the data using the provided password using the cryptography module.
    If the pasword or data is incorrect this will return None.
    """

    password = bytes(password)

    #Salt is equal to password as we want the encryption to be reversible only
    #using the password itself
    kdf = PBKDF2HMAC(algorithm=hashes.AES(),
                     length=32,
                     salt=bytes(password),
                     iterations=100000,
                     backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    token = f.decrypt(data)
    return token

def decrypt1(data, password):
    """Decrypts data using the password.

    Decrypts the data using the provided password using the cryptography module.
    If the pasword or data is incorrect this will return None.
    """

    password = bytes(password)

    #Salt is equal to password as we want the encryption to be reversible only
    #using the password itself
    kdf = PBKDF2HMAC(algorithm=hashes.AES(),
                     length=32,
                     salt=bytes(password),
                     iterations=100000,
                     backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    token = f.decrypt(data)
    return token

if __name__ == '__main__':
    #enc1('BlueBird')
    #v("ZZSSSS")
    # passwordtokey()
    # print('b\'ytviHHtklMGhEZnzd6HDmsUkrh7EFX64M2VgWVsIOYI='')
    # key ='6cCU9rXqxbDxNK0ljKu6EUP0p-dWeM8RvNGFMtYNAf4='
    # f = Fernet(key.encode())
    # print (f.encrypt("my msg"))

    # passwordtokey()
    # print('b\'ytviHHtklMGhEZnzd6HDmsUkrh7EFX64M2VgWVsIOYI='')
    #key = b'TQiXP4sAH4BCfrZfNyS1TtLtWsph-KzQlQ6Yuo_Sf1g='
    #f = Fernet(bytes(key, 'utf-8'))
    #print(f.encrypt("my msg"))
    # print(encode('mypassorg', 'XXXX'))
    #get_decryped_password('morrisonsAuthentication','gAAAAABc4tz_rL0BtbaL3h6lhIqJeZQWDZIiR01kd6qolRriMwbicOjN4ehluzjL3V_eUkeWOz3F31pUAYmRydlddSJ_uRDjQA==')
    enc1('postgres')
    #enc1d("gAAAAABc9ovWLrriYP0VbzfMrvAc3fqyEF-ACnlzbhqHbhpE6_sIlhhs6qQHPo7c-1mkvB8uOnAUIotvoViwN6ps9ixxciVW5w==")
    #print(get_decryped_password("morrisonsAuthentication","gAAAAABc4ttHT2miTgLmYFeFaFauG5lYKTWHgseLUQ6djFnpLKJnicPp5y00-1yqAj_LpUozJlQN6yRp7jc_rv7eO-thAulYHNxaWZSnjdu0c0YNIjFU-iw="))
    #decrypt('gAAAAABc4tz_rL0BtbaL3h6lhIqJeZQWDZIiR01kd6qolRriMwbicOjN4ehluzjL3V_eUkeWOz3F31pUAYmRydlddSJ_uRDjQA==','morrisonsAuthentication')
    #decrypt1('gAAAAABc4tz_rL0BtbaL3h6lhIqJeZQWDZIiR01kd6qolRriMwbicOjN4ehluzjL3V_eUkeWOz3F31pUAYmRydlddSJ_uRDjQA==','morrisonsAuthentication')

