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