import cryptography
from passlib.hash import des_crypt # crypt is deprecated

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = des_crypt.using(salt=salt).hash(word)
        if (cryptWord == cryptPass):
            print(f"[+] Found Password: {word}\n")
            return
    print("[-] Password Not Found.\n")
    return

def main():
    
