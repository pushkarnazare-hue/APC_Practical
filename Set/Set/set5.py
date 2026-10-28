students5 = {"Amit", "Rehan", "Soham", "Nisarg"}
search_name = input("Enter a student name to check: ")
if search_name in students5:
    print(search_name, "exists in the set")
else:
    print(search_name, "does not exist in the set")