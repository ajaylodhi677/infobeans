from models import Book

books=[]

n=int(input("Enter number of books:"))

for i in range(n):
    print(f"Enter details for book {i+1}")
    book_id=int(input("Enter book id:"))
    book_name=input("Enter book name:")
    author=input("Enter author:")
    price=int(input("Enter price:"))

    book=Book(book_id,book_name,author,price)
    books.append(book)

print("\nAll Books:")
Book.display(books)

book_id=int(input("\nSearch Book Id:"))

print("\nBook Found:")
Book.search(books,book_id)

author=input("\nEnter author name:")

print(f"\nBooks by {author}:")
Book.by_author(books,author)

print("\nBooks with price greater than 500:")
Book.price_greater_than_500(books)

print("\nMost Expensive Book:")
Book.most_expensive(books)

print("\nAverage Price:")
Book.average_price(books)