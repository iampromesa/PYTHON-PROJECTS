from email import message
import rsa

publicKey, privateKey = rsa.newkeys(512)

message = "Hello Promesa"

encMessage = rsa.encrypt(message.encode(), publicKey)

print("Original String: ", message)
print("Encrypted String: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode

