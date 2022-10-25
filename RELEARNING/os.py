from genericpath import isfile
import os.path

if os.path.isfile("Name.txt"):
    print("Names.txt exists")
else:
    print("It does not exist")