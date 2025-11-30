import json

books = []   

def load_data():
    global books
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except:
        books = []   



def save_data():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    print("\n--- Add New Book ---")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "status": "available"
    }

    books.append(book)
    save_data()
    print("Book added successfully!\n")


def view_books():
    print("\n--- All Books ---")
    if len(books) == 0:
        print("No books available!\n")
        return
    
    for b in books:
        print("Title:", b["title"])
        print("Author:", b["author"])
        print("ISBN:", b["isbn"])
        print("Status:", b["status"])
        print("---------------------------")
    print()

def search_book():
    print("\n--- Search Book ---")
    key = input("Enter Title or ISBN: ")

    for b in books:
        if b["title"] == key or b["isbn"] == key:
            print("\nBook Found:")
            print("Title:", b["title"])
            print("Author:", b["author"])
            print("ISBN:", b["isbn"])
            print("Status:", b["status"], "\n")
            return

    print("No book found!\n")


def issue_book():
    print("\n--- Issue Book ---")
    isbn = input("Enter ISBN: ")

    for b in books:
        if b["isbn"] == isbn:
            if b["status"] == "available":
                b["status"] = "issued"
                save_data()
                print("Book issued successfully!\n")
            else:
                print("Book already issued!\n")
            return
    
    print("Book not found!\n")


def return_book():
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN: ")

    for b in books:
        if b["isbn"] == isbn:
            if b["status"] == "issued":
                b["status"] = "available"
                save_data()
                print("Book returned successfully!\n")
            else:
                print("This book is not issued!\n")
            return
    
    print("Book not found!\n")


def menu():
    load_data()   
    while True:
        print("====== Library Menu ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()