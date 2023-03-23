from sys import argv
import os

script, filename = argv

if os.path.exists(filename):
    if os.path.isfile(filename):
        print(filename, "- file")
    elif os.path.isdir(filename):
        print(filename, "- dir")
else:
    print(filename, "- not exist")