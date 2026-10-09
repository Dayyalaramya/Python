contacts = {}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print("\n--- Contact Book ---")

for name, phone in contacts.items():
    print("Name:", name)
    print("Phone:", phone)