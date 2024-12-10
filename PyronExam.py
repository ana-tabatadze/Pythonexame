class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

def main():
    book_manager = BookManager()

    while True:
        print("\n1. დაამატე წიგნი")
        print("2. წიგნების ჩამონათვალი")
        print("3. იპოვე წიგნი")
        print("4. გასვლა")

        choice = input("შეიყვანე შენი რიცხვი: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))
            book = Book(title, author, year)
            book_manager.add_book(book)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            title = input("Enter book title to find: ")
            book = book_manager.find_book_by_title(title)
            if book:
                print(f"Found book: {book.title}")
            else:
                print("Book not found")
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()