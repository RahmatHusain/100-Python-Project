# 🔍 Duplicate File Finder

> A Python automation tool that detects duplicate files using file hashing.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📖 Overview

Duplicate files waste storage space and make file management difficult.

This project scans a folder, generates a unique hash for each file, and identifies duplicate files based on identical content.

---

## ✨ Features

- 🔍 Detect duplicate files
- ⚡ Fast MD5 hashing
- 📁 Folder scanning
- 📄 Generate scan report
- 🛡 Error handling included
- 🚀 Beginner-friendly project

---

## 📂 Project Structure

```text
duplicate-file-finder/
│── main.py
│── README.md
│── duplicates_report.txt
└── test_files/
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/RahmatHusain/100-Python-Project.git
```

### Navigate to Project

```bash
cd duplicate-file-finder
```

### Run Program

```bash
python main.py
```

---

## 📸 Example Folder

### Before Scan

```text
test_files/

photo.jpg
photo_copy.jpg
resume.pdf
movie.mp4
movie_copy.mp4
```

---

## 📊 Example Output

```text
🔍 Duplicate File Scan Results
-----------------------------------

📄 Duplicate: photo_copy.jpg
📌 Original : photo.jpg

📄 Duplicate: movie_copy.mp4
📌 Original : movie.mp4
```

---

## 📄 Report File

The program automatically generates:

```text
duplicates_report.txt
```

Example:

```text
Duplicate: photo_copy.jpg
Original : photo.jpg

Duplicate: movie_copy.mp4
Original : movie.mp4
```

---

## 🛠 Technologies Used

- Python
- os
- hashlib

---

## 📚 Concepts Learned

- File Handling
- Hashing (MD5)
- Functions
- Dictionaries
- Error Handling
- Automation Scripts

---

## 🚀 Future Improvements

- Delete duplicate files
- GUI using Tkinter
- Export to CSV
- Folder selection by user
- Calculate storage saved

---

## 👨‍💻 Author

**Rahmat Husain**

- 🎓 BIT Student
- 💻 Python Developer
- 🚀 Learning Automation & Software Development

⭐ If you like this project, give it a star!