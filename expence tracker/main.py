import json

print("=== Expense Tracker ===")

expenses = []

# Load data safely
try:
    with open("data.json", "r") as file:
        expenses = json.load(file)
        if not isinstance(expenses, list):
            expenses = []
except:
    expenses = []

while True:
    amount = input("Enter amount (or 'q' to quit): ")

    if amount.lower() == "q":
        break

    # validate number
    try:
        amount = float(amount)
    except ValueError:
        print("❌ Invalid amount. Enter a number.")
        continue

    # category input (STRICT)
    category = input("Enter category (food, travel, etc): ").strip()

    if not category:
        print("❌ Category cannot be empty.")
        continue

    expenses.append({
        "amount": amount,
        "category": category
    })

# SAVE DATA
with open("data.json", "w") as file:
    json.dump(expenses, file, indent=4)

# DISPLAY OUTPUT
print("\n--- Expense Summary ---")

if len(expenses) == 0:
    print("No expenses found.")
else:
    for expense in expenses:
        print(f"{expense['category']} : {expense['amount']}")

    total = sum(float(e["amount"]) for e in expenses)
    print("\nTotal spent:", total)