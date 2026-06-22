import json

print("=== Expense Tracker ===")

expenses = []

# Load old data safely
try:
    with open("data.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []

while True:
    amount = input("Enter amount (or 'q' to quit): ")

    # Exit condition
    if amount.lower() == "q":
        break

    # ERROR HANDLING: check valid number
    try:
        amount = float(amount)
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        continue

    category = input("Enter category: ")

    # Prevent empty category
    if category.strip() == "":
        print("❌ Category cannot be empty.")
        continue

    expenses.append({
        "amount": amount,
        "category": category
    })

# Show summary safely
print("\n--- Expense Summary ---")

total = 0

for expense in expenses:
    try:
        total += float(expense["amount"])
        print(expense["category"], ":", expense["amount"])
    except:
        print("Skipping invalid record:", expense)

print("\nTotal spent:", total)

# Save data safely
with open("data.json", "w") as file:
    json.dump(expenses, file)