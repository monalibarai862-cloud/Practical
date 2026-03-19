class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book name: ")
        self.books.append(Book(title))
        print("Book added!")

    def show_books(self):
        print("\nBooks List:")
        for b in self.books:
            status = "Issued" if b.is_issued else "Available"
            print(b.title, "-", status)

    def issue_book(self):
        name = input("Enter book to issue: ")
        for b in self.books:
            if b.title == name and not b.is_issued:
                b.is_issued = True
                print("Book issued!")
                return
        print("Book not available")

    def return_book(self):
        name = input("Enter book to return: ")
        for b in self.books:
            if b.title == name and b.is_issued:
                b.is_issued = False
                print("Book returned!")
                return
        print("Invalid book name")


# Menu-driven program
lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.show_books()
    elif choice == 3:
        lib.issue_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        break
    else:
        print("Invalid choice")