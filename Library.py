from book import Book

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+", encoding = "utf-8")
    
    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books_list = self.file.read().splitlines()

        if not books_list:
            print("\nThere are no books in the library")
            return
        
        print("\nBooks in the library:")
        for line in books_list:
            book_info = line.split(",")
            print(f"Book name: {book_info[0]} | Author: {book_info[1]}")

    def add_book(self):
        print("\n===Adding a book to the library===")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter book release year: ")
        pages = input("Enter book number of pages: ")

        book_line = f"{title},{author},{release_year},{pages}\n"
        
        self.file.write(book_line)
        print("\n{title} added to the library successfully")

    def remove_book(self):
        print("\n===Removing a book from the library===")
        title_to_remove = input("Enter book title: ")

        self.file.seek(0)
        books_list = self.file.read().splitlines()

        updated_books = []
        book_found = False

        for line in books_list:
            book_info = line.split(",")
            if book_info[0].strip().lower() == title_to_remove.strip().lower():
                book_found = True
                continue
            updated_books.append(line)

        if not book_found:
            print("\n{title_to_remove} not found in the library!") 
            return
        
        self.file.seek(0)
        self.file.truncate()
        
        for line in updated_books:
            self.file.write(line + "\n")

        print("\n{title_to_remove} removed from the library successfully")
