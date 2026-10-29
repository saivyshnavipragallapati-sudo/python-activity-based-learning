
bills = []
n = int(input("Enter number of months: "))
for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units!")
        continue
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill = bill + 50
    if units > 200:
        bill = bill + bill * 0.0
    if units < 100:
        bill = bill - bill * 0.05

    bills.append(bill)

    print("Monthly Bill: Rs.", round(bill, 2))
print("\n--- Monthly Bill Comparison ---")

for i in range(len(bills)):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 0:
            print("Increase: Rs.", round(increase, 2))
        elif increase < 0:
            print("Decrease: Rs.", round(abs(increase), 2))
        else:
            print("No change")

        if bills[i] > bills[i - 1] * 1.5:
            print("Warning: Unusual bill increase!")

