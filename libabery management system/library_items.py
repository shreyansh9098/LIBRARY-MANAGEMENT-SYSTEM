class LibraryItem:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False
        self.due_date = None

    def check_out(self, due_date):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.due_date = due_date
            print(f"{self.title} has been checked out. Due date: {due_date}")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.due_date = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, category, pages):
        super().__init__(title, author, category)
        self.pages = pages


class Magazine(LibraryItem):
    def __init__(self, title, author, category, issue):
        super().__init__(title, author, category)
        self.issue = issue


class DVD(LibraryItem):
    def __init__(self, title, director, category, duration):
        super().__init__(title, director, category)
        self.duration = duration