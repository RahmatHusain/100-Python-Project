import os
import hashlib

folder_path = "test_files"
files = os.listdir(folder_path)

print(files)

def get_file_hash(file_path):

    hasher = hashlib.md5()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()
file_hashes = {}
duplicates = []