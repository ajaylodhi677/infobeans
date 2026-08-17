'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
'''
book = set()
while True:
    print("\n========== LIBRARY ISBN MANAGER ==========")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            n = int(input("Enter number of books: "))
            for i in range(n):
                isbn = input("Enter the ISBN Number: ")
                book.add(isbn)
        case 2:
            isbn = input("Enter ISBN to remove: ")
            if isbn in book:
                book.remove(isbn)
                print("ISBN removed successfully.")
            else:
                print("ISBN not found.")
        case 3:
            isbn = input("Enter ISBN to search: ")
            if isbn in book:
                print("ISBN" , isbn, "Foudn in library")
            else:
                print("ISBN not found.")
        case 4:
            print("ISBN List:", book)
        case 5:
            print("Total Books:", len(book))
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")