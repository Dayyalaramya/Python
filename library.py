books = ["Python", "Java", "C", "SQL"]

print("Available Books:")
for book in books:
    print(book)

book_name = input("Enter the book you want: ")

if book_name in books:
    print("Book is available.")

    choice = input("Do you want to borrow it? (yes/no): ")

    if choice.lower() == "yes":
        books.remove(book_name)
        print("Book borrowed successfully.")
    else:
        print("Thank you!")
else:
    print("Book is not available.")

print("Remaining books:", books)