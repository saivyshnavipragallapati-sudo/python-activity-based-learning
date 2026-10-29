
budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expense categories: "))
total_spending = 0
expenses = {}
for i in range(n):
    print("\nExpense", i + 1)
    category = input("Enter category (food/hotel/transport/shopping): ")
    amount = float(input("Enter expense amount in foreign currency: "))
    rate = float(input("Enter exchange rate (INR per unit): "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    converted_amount = amount * rate
    fee = converted_amount * fee_percent / 100
    total = converted_amount + fee
    expenses[category] = total
    total_spending += total
    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(total, 2))

print("\n--- Travel Budget Report ---")
print("Budget: Rs.", round(budget, 2))
print("Total Spending: Rs.", round(total_spending, 2))

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

largest = max(expenses, key=expenses.get)
print("Largest Expense Category:", largest)

if total_spending <= budget:
    print("Budget Status: Within Budget")
    print("Remaining Amount: Rs.", round(budget - total_spending, 2))
else:
    print("Budget Status: Over Budget")
    print("Extra Amount: Rs.", round(total_spending - budget, 2))

