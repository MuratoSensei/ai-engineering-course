from library import Library

def main():
    lib = Library()

    while True:
        print("""
        1. List books
        2. Add book
        3. Remove book
        4. Exit
        """)
    
        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
