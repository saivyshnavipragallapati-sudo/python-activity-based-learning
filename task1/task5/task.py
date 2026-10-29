
usage = float(input("Enter monthly data usage in GB: "))
days = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget in Rs: "))
plans = [
    ["Plan A", 199, 2, 28, 50],
    ["Plan B", 299, 5, 56, 30],
    ["Plan C", 399, 10, 84, 20]
]
best_plan = ""
lowest_cost = float("inf")
for plan in plans:
    name, price, data, validity, extra = plan
    excess = max(0, usage - data)
    total = price + excess * extra
    print("\n", name)
    print("Plan Price: Rs.", price)
    print("Excess Charges: Rs.", excess * extra)
    print("Total Cost: Rs.", total)
    if validity >= days and total <= budget:
        if total < lowest_cost:
            lowest_cost = total
            best_plan = name
print("\n--- Best Plan ---")

if best_plan:
    print("Most Economical Plan:", best_plan)
    print("Total Cost: Rs.", lowest_cost)
else:
    print("No plan satisfies your budget and validity.")

