class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' is now borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is not currently borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' in their borrowed books list.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

def library_system():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    member = LibraryMember("Eric Rono", "M123")

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable books to borrow:")
            available_books = [book for book in [book1, book2, book3] if not book.is_borrowed]
            for i, book in enumerate(available_books, start=1):
                print(f"{i}. {book.title} by {book.author}")

            book_choice = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= book_choice < len(available_books):
                member.borrow_book(available_books[book_choice])
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("\nBooks you have borrowed:")
            for i, book in enumerate(member.borrowed_books, start=1):
                print(f"{i}. {book.title} by {book.author}")

            book_choice = int(input("Enter the number of the book to return: ")) - 1
            if 0 <= book_choice < len(member.borrowed_books):
                member.return_book(member.borrowed_books[book_choice])
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid option. Please select a valid choice.")

library_system()
