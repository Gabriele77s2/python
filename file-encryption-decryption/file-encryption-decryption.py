from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

generate_key()  # Run this once to generate a key

while True:
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        file_to_encrypt = input("Enter filename to encrypt: ")
        key = load_key()
        encrypt_file(file_to_encrypt, key)
        print(f"{file_to_encrypt} encrypted.")
    elif choice == '2':
        file_to_decrypt = input("Enter filename to decrypt: ")
        key = load_key()
        decrypt_file(file_to_decrypt, key)
        print(f"{file_to_decrypt} decrypted.")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
