import cryptography

def testPass(cryptPass):
    salt = cryptPass[0:2]
    