name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))
salarygross = basic + allowances + overtime 
if gross <= 20000:    deduction = gross * 0.05elif gross <= 50000: 
deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:  
deduction = (20000 * 0.05 +                 30000 * 0.10 +                 (gross - 50000) * 0.15)
print("\n===== SALARY STATEMENT =====")
print("Employee Name :", name)
print("Basic Salary  : Rs.", basic)
print("Allowances    : Rs.", allowances)
print("Overtime Pay  : Rs.", overtime)
print("Incentives    : Rs.", incentives)
print("----------------------------")
print("Gross Salary  : Rs.", round(gross, 2))
print("Deductions    : Rs.", round(deduction, 2)
Enter employee name: Ravi
Enter basic salary: 25000
Enter allowances: 5000
Enter overtime pay: 2000
Enter incentives: 3000
===== SALARY STATEMENT =====
Employee Name : Ravi
Basic Salary  : Rs. 25000.0
Allowances    : Rs. 5000.0
Overtime Pay  : Rs. 2000.0
Incentives    : Rs. 3000.0
Gross Salary  : Rs. 35000.0
Deductions    : Rs. 2500.0
Net Salary    : Rs. 32500.0
1. Input: Read basic pay, allowances, overtime, and incentives.
2. Gross salary: Add all four amounts.
3. Progressive deductions:
   - Up to ₹20,000: 5%.
   - ₹20,001–₹50,000: 5% on the first ₹20,000 and 10% on the remaining amount.
   - Above ₹50,000: Apply 15% to the amount above ₹50,000, along with the lower deductions.
4. Net salary: Subtract deductions from gross salary.
5. Salary statement: Print the employee's salary details.
