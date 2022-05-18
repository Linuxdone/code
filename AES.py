from Crypto.Cipher import AES
def paddedText(text):
    while len(text) % 16 !=0:
        text+=''
    return text
def paddedKey(key):
    while len(key) %8 != 0:
        key+=''
    return key            

plain_text = input("Enter plain text: ")
plain = paddedText(plain_text)
plain_key = input(" Enter key between 16 to 32")
key = paddedKey(plain_key) 
if len(plain_key) < 16 & len(plain_key)>32:
    print("Key shoulde be between 16 to 32")

cipher = AES.new(key.encode('utf8'),AES.MODE_ECB)
cipher_text = cipher.encrypt(plain)
print('Cipher Text: %r' %cipher_text)
decrpyted = cipher.decrypt(cipher_text)
print('Decrypted Text: %r' %decrpyted)

