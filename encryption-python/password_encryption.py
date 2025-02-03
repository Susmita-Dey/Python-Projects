from cryptography.fernet import Fernet
import rsa

# taking input string
password = input("Enter the password you want to encrypt: ")

print(
    "Encryption can be done in 2 ways: symmetric and assymetric.\n Input 1 to choose \'Symmetric-key Encryption\' and 2 to choose \'Asymmetric-key Encryption\'"
)
choice = int(input("Enter your choice: "))

if choice == 1:
    # generating encryption key
    key = Fernet.generate_key()

    # instance the Fernet class with the key
    fernet = Fernet(key)

    # encrypting the password given by the user
    encryptedPassword = fernet.encrypt(password.encode())

    # decrypt password to see if it's working or not
    # decryptedPassword = fernet.decrypt(password).decode()

elif choice == 2:
    # generate public and private keys
    publicKey, privateKey = rsa.newkeys(512)

    # encrypting the password given by the user
    encryptedPassword = rsa.encrypt(password.encode(), publicKey)

    # decrypt password to see if it's working or not
    # decryptedPassword = rsa.decrypt(password, privateKey).decode()

print("\nOriginal password: " + str(password))
print("Encrypted password: " + str(encryptedPassword))
# print("Decrypted password: " + decryptedPassword)
