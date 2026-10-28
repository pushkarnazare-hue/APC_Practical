available_books = {"Python Basics", "Data Structures", "DBMS", "Networks"}
requested_books = {"DBMS", "Operating Systems", "Python Basics"}
available_requested = requested_books & available_books
print("Requested books that are available:", available_requested)