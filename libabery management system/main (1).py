from library import Library
from library_items import Book, Magazine, DVD
from student import Student
from utils import calculate_fine

# Main program logic
library = Library()
current_student = None

while True:
    print("\nLibrary Management System")
    if current_student is None:
        print("1. Register as a new student")
        print("2. Login as an existing student")
    else:
        print(f"Logged in as: {current_student.name}")
        print("3. Add item")
        print("4. Search item")
        print("5. Check out item")
        print("6. Return item")
        print("7. Calculate fine")
        print("8. Logout")

    choice = input("Enter your choice: ")

    if choice == '1' and current_student is None:
        name = input("Enter your name: ")
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        Student.register(name, username, password)

    elif choice == '2' and current_student is None:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        current_student = Student.login(username, password)
        if current_student is None:
            print("Login failed. Please check your username and password.")

    elif choice == '3' and current_student is not None:
        item_type = input("Enter item type (book/magazine/dvd): ").lower()
        title = input("Enter title: ")
        author = input("Enter author: ")
        category = input("Enter category: ")

        if item_type == "book":
            pages = input("Enter number of pages: ")
            library.add_item(Book(title, author, category, pages))
        elif item_type == "magazine":
            issue = input("Enter issue number: ")
            library.add_item(Magazine(title, author, category, issue))
        elif item_type == "dvd":
            duration = input("Enter duration: ")
            library.add_item(DVD(title, author, category, duration))
        else:
            print("Invalid item type. Please choose from book, magazine, or dvd.")

    elif choice == '4' and current_student is not None:
        query = input("Enter title or author to search: ")
        library.search_item(query)

    elif choice == '5' and current_student is not None:
        title = input("Enter title to check out: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        library.check_out_item(title, due_date)

    elif choice == '6' and current_student is not None:
        title = input("Enter title to return: ")
        return_date = input("Enter return date (YYYY-MM-DD): ")
        if library.return_item(title):
            calculate_fine(library.get_due_date(title), return_date)

    elif choice == '7' and current_student is not None:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        return_date = input("Enter return date (YYYY-MM-DD): ")
        calculate_fine(due_date, return_date)

    elif choice == '8' and current_student is not None:
        print(f"Logging out {current_student.name}.")
        current_student = None

    elif choice == '6' and current_student is None:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")