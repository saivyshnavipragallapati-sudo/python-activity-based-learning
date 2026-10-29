
product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))
material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost: "))
selling_price = float(input("Enter selling price per unit: "))
target_profit = float(input("Enter target profit: "))
material_cost = material * quantity
wastage_cost = material_cost * wastage_percent / 100
labour_cost = labour * quantity
total_cost = material_cost + wastage_cost + labour_cost + machine
revenue = selling_price * quantity
profit = revenue - total_cost
print("\n--- Manufacturing Report ---")
print("Product:", product)
print("Quantity:", quantity)
print("Material Cost: Rs.", round(material_cost, 2))
print("Wastage Cost: Rs.", round(wastage_cost, 2))
print("Labour Cost: Rs.", round(labour_cost, 2))
print("Machine Cost: Rs.", round(machine, 2))
print("Total Production Cost: Rs.", round(total_cost, 2))
print("Total Sales Revenue: Rs.", round(revenue, 2))
print("Profit/Loss: Rs.", round(profit, 2))
if profit >= target_profit:
    print("Result: Profit target achieved!")
else:
    print("Result: Profit target not achieved.")

if quantity > 0:
    print("Cost per unit: Rs.", round(total_cost / quantity, 2))
    print("Profit per unit: Rs.", round(profit / quantity, 2))

