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

for file in files:

    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    file_hash = get_file_hash(file_path)

    if file_hash in file_hashes:
        duplicates.append(file)

    else:
        file_hashes[file_hash] = file

print("\nDuplicate Files")

if duplicates:

    for file in duplicates:
        print(file)

else:

    print("No duplicate files found.")

os.remove(file_path)