import os

with open("file.txt") as file:
    print(file.read())

os.remove("file.txt")