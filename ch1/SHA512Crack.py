import cryptography
from passlib.hash import sha512_crypt # crypt is deprecated

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = sha512_crypt.using(salt=salt).hash(word)
        if (cryptWord == cryptPass):
            print(f"[+] Found Password: {word}\n")
            return
    print("[-] Password Not Found.\n")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print(f"[*] Cracking Password For: {user}\n")
            testPass(cryptPass)

if __name__ == "__main__":
    main()
