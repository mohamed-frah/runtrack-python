def cryptage(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_crypter = ""
    
    for i in message:
        if i == " ":
            message_crypter += " "
        else :
            index = alphabet.index(i)
            message_crypter += alphabet[(index+key) % 26]
    return message_crypter

print(cryptage("bonjour",1))
print(cryptage("hello ca va",3))