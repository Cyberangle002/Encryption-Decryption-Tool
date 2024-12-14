from cryptography.fernet import Fernet

# Generate a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
generate_key()  # Run this once to generate a key file
message = "Hello, World!"
encrypted = encrypt_message(message)
print("Encrypted:", encrypted)

decrypted = decrypt_message(encrypted)
print("Decrypted:", decrypted)
