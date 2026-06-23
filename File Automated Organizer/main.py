import os
import shutil

path = input("Enter your path : ")

files = os.listdir(path)
for i in files:
    print(i)
for i in files:
    filename , extension = os.path.splitext(i)
    extension_1 = extension[1:]