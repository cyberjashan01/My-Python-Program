library = {
    "001": {"title": "The Great Gatsby", "copies": 5},
    "002": {"title": "To Kill a Mockingbird", "copies": 3},
    "003": {"title": "1984", "copies": 4},
}

def display_books():
    print("\nAvailable Books:")
    for book_id, details in library.items():
        print(f"ID: {book_id}, Title: {details['title']}, Copies: {details['copies']}")

def manage_books(action):
    book_id = input("\nEnter Book ID: ")
    if book_id not in library:
        print("Book not found.")
        return
    if action == "issue":
        if library[book_id]["copies"] > 0:
            library[book_id]["copies"] -= 1
            print(f"Book '{library[book_id]['title']}' issued successfully!")
        else:
            print("No copies available.")
    elif action == "return":
        library[book_id]["copies"] += 1
        print(f"Book '{library[book_id]['title']}' returned successfully!")

while True:
    print("\n1. Display Books\n2. Issue Book\n3. Return Book\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_books()
    elif choice == "2":
        manage_books("issue")
    elif choice == "3":
        manage_books("return")
    elif choice == "4":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
