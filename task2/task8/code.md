product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: ")
)material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage_percent = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost: "))
selling_price = float(input("Enter selling price per unit: "))
target_profit = float(input("Enter target profit: "))
Calculate costsmaterial_cost = material * quantitywastage_cost = material_cost * wastage_percent / 100labour_cost = labour * quantitytotal_cost = material_cost + wastage_cost + labour_cost + machinerevenue = selling_price * quantityprofit = revenue - total_costprint("\n--- Manufacturing Report ---")
print("Product:", product)print("Quantity:", quantity)print("Material Cost: Rs.", round(material_cost, 2))
print("Wastage Cost: Rs.", round(wastage_cost, 2)
)print("Labour Cost: Rs.", round(labour_cost, 2))
print("Machine Cost: Rs.", round(machine, 2))print("Total Production Cost: Rs.", round(total_cost, 2))
print("Total Sales Revenue: Rs.", round(revenue, 2))print("Profit/Loss: Rs.", round(profit, 2))if profit >= target_profit: 
print("Result: Profit target achieved!")
else:  
print("Result: Profit target not achieved.")if quantity > 0: 
print("Cost per unit: Rs.", round(total_cost / quantity, 2))
print("Profit per unit: Rs.", round(profit / quantity, ))
Enter product name: Chair
Enter quantity produced: 100
Enter material cost per unit: 200
Enter labour cost per unit: 50
Enter wastage percentage: 10
Enter total machine cost: 2000
Enter selling price per unit: 350
Enter target profit: 5000
Product: Chair
Quantity: 100
Material Cost: Rs. 20000.0
Wastage Cost: Rs. 2000.0
Labour Cost: Rs. 5000.0
Machine Cost: Rs. 2000.0
Total Production Cost: Rs. 29000.0
Total Sales Revenue: Rs. 35000.0
Profit/Loss: Rs. 6000.0
Result: Profit target achieved!
Cost per unit: Rs. 290.0
Profit per unit: Rs. 60.0
1. Material cost: Material cost per unit × quantity produced.
2. Labour cost: Labour cost per unit × quantity produced.
3. Wastage cost: Calculates the wastage percentage of the total material cost.
4. Machine cost: Adds the total machine operating cost.
5. Profit calculation: Total sales revenue − total production cost.
6. Profit target: Compares the actual profit with the target profit.
