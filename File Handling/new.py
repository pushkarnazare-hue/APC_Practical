# import csv
# import os

# roll = input("Enter Roll Number to search: ")

# found = False

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for student in reader:
#         if student["RollNo"] == roll:
#             print("\nStudent Record Found")
#             print("Roll No:", student["RollNo"])
#             print("Name:", student["Name"])
#             print("Marks:", student["Marks"])
#             found = True
#             break

# if not found:
#     print("Student record not found.")
import os

os.mkdir("MyFolder")

print("Folder created")