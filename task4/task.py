
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))
gross = basic + allowances + overtime + incentives
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05 +
                 30000 * 0.10 +
                 (gross - 50000) * 0.15)
net = gross - deduction
print("\n===== SALARY STATEMENT =====")
print("Employee Name :", name)
print("Basic Salary  : Rs.", basic)
print("Allowances    : Rs.", allowances)
print("Overtime Pay  : Rs.", overtime)
print("Incentives    : Rs.", incentives)
print("Gross Salary  : Rs.", round(gross, 2))
print("Deductions    : Rs.", round(deduction, 2))
print("Net Salary    : Rs.", round(net, 2))


