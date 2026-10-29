 Hospital Billing and Patient Classification
 name = input("Enter patient name: ")
 consultation = float(input("Enter consultation charge: "))
 diagnostic = float(input("Enter diagnostic charge: "))
 treatment = float(input("Enter treatment charge: "))
 Validate chargesif consultation < 0 or diagnostic < 0 or treatment < 0:  
 print("Invalid charges! Charges cannot be negative.")else:    
 total = consultation + diagnostic + treatment  
 if total >= 5000:      
 discount = total * 0.10  
 elif total >= 3000:     
 discount = total * 0.05 
 else:        discount = 0  
 final_bill = total - discount 
 if final_bill >= 5000:     
 category = "High Payment" 
 elif final_bill >= 2000:
 category = "Medium Payment"   
 else:        category = "Low Payment"  
Enter patient name: Ravi
Enter consultation charge: 500
Enter diagnostic charge: 1500
Enter treatment charge: 4000

--- Hospital Bill ---
Patient Name: Ravi
Consultation Charge: Rs. 500.0
Diagnostic Charge: Rs. 1500.0
Treatment Charge: Rs. 4000.0
Total Bill: Rs. 6000.0
Concession: Rs. 600.0
Final Bill: Rs. 5400.0
Patient Category: High Payment
1. Input: Enter patient details and hospital charges.
2. Validation: Reject negative charges.
3. Total bill: Add consultation, diagnostic, and treatment charges.
4. Concession: Give a 10% discount for bills of ₹5,000 or more, or 5% for bills of ₹3,000 or more.
5. Classification: Classify the patient as High, Medium, or Low Payment based on the final bill.

Note: The concession rates and payment categories are example rules for Python practice, not actual hospital policies.
