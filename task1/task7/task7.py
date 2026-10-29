
n = int(input("Enter number of products: "))
subtotal = 0
total_tax = 0
for i in range(n):
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
          "Tax:", round(tax, 2))
    subtotal += amount
    total_tax += tax
if subtotal >= 5000:
    discount_rate = 15
elif subtotal >= 2000:
    discount_rate = 10
elif subtotal >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100
max_discount = 1000
if discount > max_discount:
    discount = max_discount
final_bill = subtotal + total_tax - discount
print("\n====== ITEMIZED INVOICE ======")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))
print("==============================")

