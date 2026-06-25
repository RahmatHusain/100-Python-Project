import json
import os

FILE_NAME = "passwords.json"

# Load passwords
def load_passwords():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

# Save passwords
def save_passwords(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add password
def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = load_passwords()

    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("✅ Password saved successfully!")

# View password
def view_password():
    website = input("Enter website name: ")

    data = load_passwords()

    if website in data:
        print("\nWebsite :", website)
        print("Username:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("❌ No password found.")

# Main menu
while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option.")