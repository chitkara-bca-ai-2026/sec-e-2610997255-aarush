print("================================")
print("   CLOTHING STORE BILLING SYSTEM")
print("================================")

customer = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total = price * quantity

print("================================")
print("             BILL")
print("================================")
print("Customer Name :", customer)
print("Garment Name  :", garment)
print("Price per Unit: Rs.", price)
print("Quantity      :", quantity)
print("Total Amount  : Rs.", total)
print("================================")
