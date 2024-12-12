import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, წელი: {self.year}"

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
                raise ValueError("წელი უნდა იყოს დადებითი მთელი რიცხვი")
            self.books.append(Book(title, author, year))
            print("წიგნი წარმატებით დამატდა!")
        except ValueError as e:
            print(f"არასწორი წელი: {e}")

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
        print("\n1. წიგნის დამატება")
        print("2. ყველა წიგნის ჩვენება")
        print("3. წიგნის ძებნა")
        print("4. გასვლა")

        choice = input("ასარჩევად შეიყვანეთ რიცხვი: ")

        if choice == '1':
            title = input("შეიყვანეთ წიგნის სათაური: ")
            author = input("შეიყვანეთ ავტორი: ")
            year = input("შეიყვანეთ გამოცემის წელი: ")
            book_manager.add_book(title, author, year)

        elif choice == '2':
            book_manager.show_all_books()

        elif choice == '3':
            title = input("შეიყვანეთ წიგნის სათაური ძებნისთვის: ")
            book = book_manager.find_book_by_title(title)
            if book:
                print(book)
            else:
                print("წიგნი ვერ მოიძებნა.")

        elif choice == '4':
            book_manager.save_books()
            break

        else:
            print("არასწორი რიცხვი. გთხოვთ სცადოთ ხელახლა.")

if __name__ == "__main__":
    main()