# Progressive Electricity Billing – Python Program

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on multiple electricity consumption slabs. The program should include fixed charges, surcharges, and rebates.

The program should also:

- Accept electricity consumption for several months.
- Calculate charges based on different consumption slabs.
- Add fixed charges and surcharges.
- Apply rebates when applicable.
- Calculate the final monthly electricity bill.
- Compare electricity bills across different months.
- Identify unusual increases in electricity bills.

## 2. Algorithm

1. Start the program.
2. Enter the number of months.
3. Initialize the previous month's bill and total bill.
4. For each month, enter the electricity consumption in units.
5. Calculate electricity charges using progressive slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
6. Add fixed charges of ₹100.
7. Calculate a 5% surcharge on the energy charges.
8. Apply a 10% rebate if consumption is below 100 units.
9. Calculate the final electricity bill.
10. Compare the current month's bill with the previous month's bill.
11. Identify unusual increases if the bill increases by more than 25%.
12. Display the monthly bills and total bill.
13. Stop the program.
 ## 3.Flowchart
``` mermaid

flowchart TD
    A([START]) --> B[/Enter Number of Months/]
    B --> C[Initialize Total Bill = 0]
    C --> D[/Enter Month and Units Consumed/]
    D --> E{Units <= 100?}
    E -- Yes --> F[Energy Charge = Units * 2]
    E -- No --> G{Units <= 200?}
    G -- Yes --> H[Charge = 100*2 + Remaining*3]
    G -- No --> I[Charge = 100*2 + 100*3 + Remaining*5]
    F --> J[Add Fixed Charge]
    H --> J
    I --> J
    J --> K[Calculate 5% Surcharge]
    K --> L{Units < 100?}
    L -- Yes --> M[Apply 10% Rebate]
    L -- No --> N[No Rebate]
    M --> O[Calculate Final Bill]
    N --> O
    O --> P[Add Bill to Total]
    P --> Q{More Months?}
    Q -- Yes --> D
    Q -- No --> R[Compare Monthly Bills]
    R --> S[Identify Increases Above 25%]
    S --> T[/Display Monthly and Total Bills/]
    T --> U([STOP])
```
## 5. Sample Input
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units consumed: 80

Month 2
Enter month name: February
Enter electricity units consumed: 150

Month 3
Enter month name: March
Enter electricity units consumed: 250
## 6. Sample Output
Month: January
Energy Charge: Rs. 160.0
Fixed Charge: Rs. 100
Surcharge: Rs. 8.0
Rebate: Rs. 26.8
Final Bill: Rs. 241.2

Month: February
Energy Charge: Rs. 350.0
Fixed Charge: Rs. 100
Surcharge: Rs. 17.5
Rebate: Rs. 0
Final Bill: Rs. 467.5

Warning: Unusual Bill Increase!
Change: 93.82 %

Month: March
Energy Charge: Rs. 650.0
Fixed Charge: Rs. 100
Surcharge: Rs. 32.5
Rebate: Rs. 0
Final Bill: Rs. 782.5

Warning: Unusual Bill Increase!
Change: 67.38 %

----- ELECTRICITY BILL SUMMARY -----
Total Electricity Bill: Rs. 1491.2
Average Monthly Bill: Rs. 497.07
Number of Months: 3
```
