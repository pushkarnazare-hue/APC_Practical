from books import catalog
from members import registration
from transactions import issue_return

catalog.add_book(1, "Python Basics", "John Doe")
registration.register_member(1, "Ravi")

catalog.display_books()
registration.display_members()

book = catalog.books_list[0]
member = registration.members_list[0]

issue_return.issue_book(book, member)
issue_return.return_book(book)
