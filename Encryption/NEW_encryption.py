import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time
import os
from cryptography.fernet import InvalidToken

password_provided = input("Password: ")  # This is input in the form of a string
mode = input("Encrypt(E) or Decrypt(D): ")
password = password_provided.encode()  # Convert to type bytes
salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
print('This is the encryption key: ', key)


if mode.upper() == 'E':
    from cryptography.fernet import Fernet
    message = input("Message: ").encode()

    f = Fernet(key)
    encrypted1 = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes
    encrypted_msg = encrypted1.decode()
    print('')
    time.sleep(1)
    print(encrypted_msg)
    print('')
    time.sleep(1)
    print('Would you like to output this message into a text file??')
    choice = input('y/n: ')
    if choice == 'y':
        encrypted_file = open('encrypted_file.txt','wb')
        encrypted_file.write(encrypted1)
        os.startfile('encrypted_file.txt')

    else:
        print('Exiting Program...')
        time.sleep(1.5)
        exit()

elif mode.upper() == 'D':
    from cryptography.fernet import Fernet
    #encrypted = b"gAAAAABivoEFxAPJ5ZaWsI2t_U6vMmUcbjdzkOELUqNfhz2uQ2NQ8R1w4fBZjoF1RWBvbMjkjE-QOUQJ_VZrreoUj2s4C3NDdw=="
    encrypted2 = input("The encrypted message: ").encode()
    #file = open('encrypted_file.txt','rb')
    #encrypted = file.read()
    f = Fernet(key)
    try:
        decrypted = f.decrypt(encrypted2)  # Decrypt the bytes. The returning object is of type bytes
        decrypted_msg = decrypted.decode()
        print("Valid Key - Successfully decrypted")
        print('')
        time.sleep(1)
        print('Decrypted message: ',decrypted_msg)
    except InvalidToken as e:
        # Catch any InvalidToken exceptions if the correct key was not provided
        print('')
        time.sleep(.5)
        print('X')
        time.sleep(.5)
        print("Invalid Key - Unsuccessfully decrypted")
        time.sleep(1)
        print('Exiting the Program...')
        time.sleep(1.2)
        exit()

        
    
    print('')
    print('Would you like to exit the program??')
    choice = input('y/n: ')
    if choice == 'y':
        print('Exiting Program...')
        time.sleep(1.5)
        exit()
    else:
        input('')

else:
    print('Invalid choice, run the program and try again.')



# Video : https://www.youtube.com/watch?v=H8t4DJ3Tdrg
# The guys website were I took some of the code(in the vid description) : https://nitratine.net/blog/post/encryption-and-decryption-in-python/