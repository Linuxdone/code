
def gcd(a,b):
    while b!=0:
        c = a % b
        a = b
        b = c
    return a

def coprimes(m):
    l=[]
    for x in range(2,m):
        if gcd(m,x)==1 and modinv(x,phi)!=None:
            l.append(x)
    for x in  l:
        if x==modinv(x, phi):
            l.remove(x)
    return l


def modinv(a, m):
    for x in range(1, m):
        if (a*x)%m ==1:
            return x
    return None

def encrypt_block(s):
    e1 = e ** s%n 
    return e1

def decrypt_block(s):
    d1 = d**s%n 
    return d1

def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x)))for x in list(s)])

def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x)))for x in list(s)])

if __name__=="__main__":
    p = int(input("Enter prime number: "))
    q = int(input("Enter prime number: "))
    n=p*q
    phi=(p-1)*(q-1)
    print(str(phi))
    print(str(coprimes(phi)))
    e=int(input())
    d=modinv(e,phi)
    s=input("Enter your msg: ")
    enc = encrypt_string(s)
    print("Encrypted msg: %r", enc)
    dec = decrypt_string(enc)
    print("Decrypted msg: %r" %dec)




