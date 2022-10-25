from cryptography.fernet import Fernet

message = input("Input a message to encrypt: ")

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("Original string: ", message)
print("Encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("Decrypted string: ", decMessage)
