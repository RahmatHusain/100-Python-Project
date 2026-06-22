print("=== Expense Tracker ===")

amount = input("Enter expense amount: ")
category = input("Enter category (food, travel, etc): ")

print(amount, category)

expenses = []

amount = input("Enter amount: ")
category = input("Enter category: ")

expense = {
    "amount": amount,
    "category": category
}

expenses.append(expense)

print(expenses)

expenses = []

while True:
    amount = input("Enter amount (or 'q' to quit): ")

    if amount == "q":
        break

    category = input("Enter category: ")

    expenses.append({
        "amount": amount,
        "category": category
    })

print(expenses)

total = 0

for expense in expenses:
    total += float(expense["amount"])

print("Total spent:", total)

import json

with open("data.json", "w") as file:
    json.dump(expenses, file)

    import json

try:
    with open("data.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []

    print("\n--- Expense Summary ---")
for e in expenses:
    print(e["category"], ":", e["amount"])