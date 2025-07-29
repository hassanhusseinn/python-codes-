from cryptography.fernet import Fernet  # Note the capital F

key = Fernet.generate_key()
cipher = Fernet(key)

print("The generated key is " + key.decode())

message = input("Enter the message you want to encrypt: ")

encryptedMessage =  cipher.encrypt(message.encode())

print ("The encrypted message is " + encryptedMessage.decode())

decryptedMessage = cipher.decrypt(encryptedMessage).decode()
print ("The decrypted message is " + decryptedMessage)




