n = int(input("Enter prime number"))
g = int(input("Enter base prime number: "))
alicesecret = int(input("Enter ALice Secret Key: " ))
bobsecret = int(input("Enter Bob secret key: "))
A = (g**alicesecret)%n
B = (g**bobsecret)%n
alicesecretkey = (B**alicesecret)%n
bobsecretkey = (A**bobsecret)%n
print(alicesecretkey)
print(bobsecretkey)