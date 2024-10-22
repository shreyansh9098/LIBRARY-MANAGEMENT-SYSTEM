from library_items import Book, Magazine, DVD

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.title}")

    def search_item(self, query):
        results = [item for item in self.items if query.lower() in item.title.lower() or query.lower() in item.author.lower()]
        if results:
            for item in results:
                print(f"Found: {item.title} by {item.author}")
        else:
            print("No items found matching your search.")

    def check_out_item(self, title, due_date):
        for item in self.items:
            if item.title.lower() == title.lower():
                if not item.is_checked_out:
                    item.check_out(due_date)
                    return
                else:
                    print(f"'{item.title}' is already checked out.")
                    return
        print(f"No item titled '{title}' found.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if item.is_checked_out:
                    item.return_item()
                    return True
                else:
                    print(f"'{item.title}' was not checked out.")
                    return False
        print(f"No item titled '{title}' found.")
        return False

    def get_due_date(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item.due_date
        return None