def encrypt(message):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char == 'z':
                encrypted += 'a'
            elif char == 'Z':
                encrypted += 'A'
            else:
                encrypted += chr(ord(char) + 1)
        else:
            encrypted += char
    return encrypted

def decrypt(message):
    decrypted = ""
    for char in message:
        if char.isalpha():
            if char == 'a':
                decrypted += 'z'
            elif char == 'A':
                decrypted += 'Z'
            else:
                decrypted += chr(ord(char) - 1)
        else:
            decrypted += char
    return decrypted

original = input("Введите исходное сообщение: ")
encrypted = encrypt(original)
print("Зашифрованное сообщение:", encrypted)
    
encrypted = input("Введите зашифрованное сообщение для дешифровки: ")
original = decrypt(encrypted)
print("Дешифрованное сообщение:", original)