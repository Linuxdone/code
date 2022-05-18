import pyDes
data = input("Enter data: ")
key = input("Enter 16/24 key")
k = pyDes.triple_des(key, padmode=pyDes.PAD_PKCS5)
e = k.encrypt(data)
print("cipher text %r"%e)
print("Original text%r"%k.decrypt(e))