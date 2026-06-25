import json
import os

FILE_NAME = "passwords.json"
def load_passwords():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}

    return {}
print("===== PASSWORD MANAGER =====")
while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "3":
        print("Goodbye!")
        break