from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

while True:
    print("\n1. Generate Key\n2. Encrypt File\n3. Decrypt File\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        write_key()
        print("✅ Key generated and saved as secret.key")
    elif choice == "2":
        key = load_key()
        filename = input("Enter filename to encrypt: ")
        encrypt_file(filename, key)
        print("🔒 File encrypted successfully!")
    elif choice == "3":
        key = load_key()
        filename = input("Enter filename to decrypt: ")
        decrypt_file(filename, key)
        print("🔓 File decrypted successfully!")
    elif choice == "4":
        print("👋 Exiting program...")
        break
    else:
        print("Invalid option, try again.")