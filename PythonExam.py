import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class BookManager:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump(self.books, f)

    def add_book(self, title, author, year):
        try:
            year = int(year)
            if year <= 0:
                raise ValueError("Year must be a positive integer")
            self.books.append(Book(title, author, year))
            print("Book added successfully!")
        except ValueError as e:
            print(f"Invalid year: {e}")

    def show_all_books(self):
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

def main():
    book_manager = BookManager()

    while True:
        print("\n1. Add a book")
        print("2. Show all books")
        print("3. Find a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter year of publication: ")
            book_manager.add_book(title, author, year)

        elif choice == '2':
            book_manager.show_all_books()

        elif choice == '3':
            title = input("Enter book title to search: ")
            book = book_manager.find_book_by_title(title)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == '4':
            book_manager.save_books()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()