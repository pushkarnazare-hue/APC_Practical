def issue_book(book, member):
    if book["available"]:
        book["available"] = False
        print(f"Book '{book['title']}' issued to {member['name']}")
    else:
        print("Book not available")

def return_book(book):
    book["available"] = True
    print(f"Book '{book['title']}' returned")
