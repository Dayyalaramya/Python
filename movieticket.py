name = input("Enter your name: ")
movie = input("Enter movie name: ")
tickets = int(input("Enter number of tickets: "))

price = 150
total = tickets * price

print("\n--- Movie Ticket Details ---")
print("Name:", name)
print("Movie:", movie)
print("Tickets:", tickets)
print("Price per ticket:", price)
print("Total amount:", total)

if tickets >= 5:
    print("You are eligible for a group booking.")
else:
    print("Regular booking.")