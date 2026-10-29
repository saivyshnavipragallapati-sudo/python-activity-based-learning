n = int(input("Enter number of products: "))
subtotal = 0total_tax = 0for i in range(n):   
print("\nProduct", i + 1)   
name = input("Enter product name: ") 
category = input("Enter category (food/clothing/electronics): ").lower()  
price = float(input("Enter price per item: "))  
quantity = int(input("Enter quantity: "))  
amount = price * quantity   
if category == "food":     
tax_rate = 5  
elif category == "clothing":    
tax_rate = 5 
else:      
tax_rate = 18  
tax = amount * tax_rate / 100 
print(name, "- Amount:", round(amount, 2),      
"Tax:", round(tax, 2))    subtotal += amount    total_tax += tax# Threshold discountif subtotal >= 5000:    discount_rate = 15elif subtotal >= 2000:    discount_rate = 10elif subtotal >= 1000:   
discount_rate = 5else:  
discount_rate = 0discount = subtotal * discount_rate / 100# Maximum concession limitmax_discount = 1000if discount > max_discount: 
discount = max_discountfinal_bill = subtotal + total_tax - discountprint("\n====== ITEMIZED INVOICE ======")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))
Enter number of products: 2
Product 1
Enter product name: Rice
Enter category (food/clothing/electronics): food
Enter price per item: 100
Enter quantity: 10
Rice - Amount: 1000.0 Tax: 50.0
Product 2
Enter product name: Headphones
Enter category (food/clothing/electronics): electronics
Enter price per item: 1000
Enter quantity: 2
Headphones - Amount: 2000.0 Tax: 360.0
====== ITEMIZED INVOICE ======
Subtotal: Rs. 3000.0
Total Tax: Rs. 410.0
Discount: Rs. 300.0
Final Bill: Rs. 3110.
1. Multiple products: Accepts product names, prices, quantities, and categories.
2. Category-specific taxes: Applies 5% tax to food and clothing and 18% to electronics in this example.
3. Threshold discounts: Gives 5% discount for bills of ₹1,000 or more, 10% for ₹2,000 or more, and 15% for ₹5,000 or more.
4. Maximum concession: Limits the total discount to ₹1,000.
5. Final invoice: Adds tax to the subtotal and subtracts the discount.
