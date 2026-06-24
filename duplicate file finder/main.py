import os
import hashlib

# Folder to scan
folder_path = "test_files"

# Function to generate file hash
def get_file_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()

# Check if folder exists
if not os.path.exists(folder_path):
    print(f"❌ Folder '{folder_path}' not found.")
    exit()

files = os.listdir(folder_path)

file_hashes = {}
duplicates = []

# Scan files
for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    try:
        file_hash = get_file_hash(file_path)

        if file_hash in file_hashes:
            duplicates.append((file, file_hashes[file_hash]))
        else:
            file_hashes[file_hash] = file

    except Exception as e:
        print(f"❌ Error processing {file}: {e}")

# Display results
print("\n🔍 Duplicate File Scan Results")
print("-" * 35)

if duplicates:
    for duplicate, original in duplicates:
        print(f"📄 Duplicate: {duplicate}")
        print(f"📌 Original : {original}")
        print("-" * 35)

else:
    print("✅ No duplicate files found.")

# Optional Report
with open("duplicates_report.txt", "w") as report:
    report.write("Duplicate File Scan Report\n")
    report.write("=" * 30 + "\n\n")

    if duplicates:
        for duplicate, original in duplicates:
            report.write(f"Duplicate: {duplicate}\n")
            report.write(f"Original : {original}\n\n")
    else:
        report.write("No duplicate files found.\n")

print("\n📄 Report saved as duplicates_report.txt")