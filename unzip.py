import zipfile
#pwd = "secet".encode("utf-8")
zFile = zipfile.ZipFile("evil.zip")
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password.encode("utf-8"))
        print(f"[+] Password = {password}\n")
        exit(0)
    except Exception as e:
        pass