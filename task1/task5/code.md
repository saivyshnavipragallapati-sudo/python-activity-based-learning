age = float(input("Enter monthly data usage in GB: "))
days = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget in Rs: "))#
Plan details: Name, Price, Data, Validity, Extra charge per GBplans = [    ["Plan A", 199, 2, 28, 50],    ["Plan B", 299, 5, 56, 30],    ["Plan C", 399, 10, 84, 20]]best_plan = ""
lowest_cost = float("inf")for plan in plans:    name, price, data, validity, extra = plan   
excess = max(0, usage - data)  
total = price + excess * extra  
print("\n", name)   
print("Plan Price: Rs.", price)  
print("Excess Charges: Rs.", excess * extra)    print("Total Cost: Rs.", total)  
if validity >= days and total <= budget:  
if total < lowest_cost:         
lowest_cost = total
       best_plan = name
Enter monthly data usage in GB: 4
Enter required validity in days: 28
Enter your budget in Rs: 500
Plan A
Plan Price: Rs. 199
Excess Charges: Rs. 100
Total Cost: Rs. 299
Plan B
Plan Price: Rs. 299
Excess Charges: Rs. 0
Total Cost: Rs. 299
Plan C
Plan Price: Rs. 399
Excess Charges: Rs. 0
Total Cost: Rs. 399
Most Economical Plan: Plan A
Total Cost: Rs. 299
1. Input: Enter data usage, required validity, and budget.
2. Compare plans: Store the price, included data, validity, and excess data charge of each plan.
3. Calculate cost: Add extra charges when usage exceeds the included data.
4. Check eligibility: Select plans that satisfy both the validity and budget requirements.
5. Find the best plan: Choose the eligible plan with the lowest total cost.

Note: All mobile plan prices and charges are example values for practicing Python.
