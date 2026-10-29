name= input("Enter patient name: ")
consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")
else:
    total = consultation + diagnostic + treatment
    if total >= 5000:
        discount = total * 0.10
    elif total >= 3000:
        discount = total * 0.05
    else:
        discount = 0
    final_bill = total - discount
    if final_bill >= 5000:
        category = "High Payment"
    elif final_bill >= 2000:
        category = "Medium Payment"
    else:
        category = "Low Payment"
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Consultation Charge: Rs.", consultation)
    print("Diagnostic Charge: Rs.", diagnostic)
    print("Treatment Charge: Rs.", treatment)
    print("Total Bill: Rs.", round(total, 2))
    print("Concession: Rs.", round(discount, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Category:", category)

