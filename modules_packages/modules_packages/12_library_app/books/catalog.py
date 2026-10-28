books_list = []

def add_book(book_id, title, author):
    books_list.append({"id": book_id, "title": title, "author": author, "available": True})

def display_books():
    for b in books_list:
        print(b)
