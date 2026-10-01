name = input("Enter customer name: ")
item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n----- Shopping Bill -----")
print("Customer:", name)
print("Item:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total)
print("-------------------------")