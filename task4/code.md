# Employee Payroll and Deduction Analysis – Python Program

## 1. Problem Statement

Write a Python program to calculate an employee's gross salary using basic pay, allowances, overtime, and incentives. Apply progressive deductions based on salary slabs and generate a formatted salary statement showing gross salary, total deductions, and net salary.

## 2. Algorithm

1. Start the program.
2. Enter employee name and basic salary.
3. Enter allowances, overtime hours, overtime rate, and incentives.
4. Calculate overtime pay.
5. Calculate gross salary.
6. Calculate progressive deductions:
   - First ₹10,000 – 0% deduction.
   - Next ₹10,000 – 5% deduction.
   - Above ₹20,000 – 10% deduction.
7. Calculate total deductions.
8. Calculate net salary.
9. Display the salary statement.
10. Stop the program.

## 3. Flowchart(mermaid) 
```
flowchart TD
    A([Start]) --> B[/Enter Employee Details/]
    B --> C[Calculate Overtime Pay]
    C --> D[Calculate Gross Salary]
    D --> E[Calculate Progressive Deductions]
    E --> F[Calculate Net Salary]
    F --> G[/Display Salary Statement/]
    G --> H([Stop])
```
## 5. Sample Input
Enter employee name: Rahul
Enter basic salary: 25000
Enter allowances: 5000
Enter overtime hours: 10
Enter overtime rate: 200
Enter incentives: 3000

## 6. Sample Output

Employee Name: Rahul
Basic Salary: Rs. 25000.0
Allowances: Rs. 5000.0
Overtime Pay: Rs. 2000.0
Incentives: Rs. 3000.

Gross Salary: Rs. 35000.0
Deductions: Rs. 2000.0
Net Salary: Rs. 33000.0




