budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expense categories: "))
total_spending = 0expenses = {}for i in range(n):   
print("\nExpense", i + 1)  
category = input("Enter category (food/hotel/transport/shopping): ") 
amount = float(input("Enter expense amount in foreign currency: ")) 
rate = float(input("Enter exchange rate (INR per unit): "))   
fee_percent = float(input("Enter conversion fee percentage: ")) 
converted_amount = amount * rate    fee = converted_amount * fee_percent / 100   
total = converted_amount + fee    expenses[category] = total    total_spending += total  
print("Converted Amount: Rs.", round(converted_amount, 2))   
print("Conversion Fee: Rs.", round(fee, 2))   
print("Total Expense: Rs.", round(total, 2))
print("\n--- Travel Budget Report ---")
print("Budget: Rs.", round(budget, 2))
print("Total Spending: Rs.", round(total_spending, 2))for category, amount in expenses.items():
print(category, ": Rs.", round(amount, 2))largest = max(expenses, key=expenses.get)
print("Largest Expense Category:", largest)if total_spending <= budget:   
print("Budget Status: Within Budget")   
print("Remaining Amount: Rs.", round(budget - total_spending, 2))
else: 
print("Budget Status: Over Budget") 
print("Extra Amount: Rs.", round(total_spending - budget)
Enter travel budget in INR: 50000
Enter number of expense categories: 3
Expense 1
Enter category (food/hotel/transport/shopping): hotel
Enter expense amount in foreign currency: 200
Enter exchange rate (INR per unit): 85
Enter conversion fee percentage: 2
Converted Amount: Rs. 17000.0
Conversion Fee: Rs. 340.0
Total Expense: Rs. 17340.0
Expense 2
Enter category (food/hotel/transport/shopping): food
Enter expense amount in foreign currency: 100
Enter exchange rate (INR per unit): 85
Enter conversion fee percentage: 2
Converted Amount: Rs. 8500.0
Conversion Fee: Rs. 170.0
Total Expense: Rs. 8670.0
Expense 3
Enter category (food/hotel/transport/shopping): transport
Enter expense amount in foreign currency: 150
Enter exchange rate (INR per unit): 85
Enter conversion fee percentage: 2
Converted Amount: Rs. 12750.0
Conversion Fee: Rs. 255.0
Total Expense: Rs. 13005.0

--- Travel Budget Report ---
Budget: Rs. 50000.0
Total Spending: Rs. 39015.0
hotel : Rs. 17340.0
food : Rs. 8670.0
transport : Rs. 13005.0
Largest Expense Category: hotel
Budget Status: Within Budget
Remaining Amount: Rs. 10985.0
1. Exchange rate conversion: Converts each foreign-currency expense into INR using the supplied exchange rate.
2. Conversion fee: Adds a fee based on the given percentage.
3. Total spending: Adds all expenses, including conversion fees.
4. Largest expense: Identifies the category with the highest total expense.
5. Budget comparison: Checks whether the total spending is within budget or exceeds it.

Note: Exchange rates and fees are entered by the user for this example; they are not live exchange rates. If you enter the same category more than once, this basic version overwrites its previous amount in the category summary.
