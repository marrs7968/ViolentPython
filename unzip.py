import zipfile
pwd = "secret".encode("utf-8")
zFile = zipfile.ZipFile("evil.zip")
zFile.extractall(pwd=pwd)