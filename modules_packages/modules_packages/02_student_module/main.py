import student

marks = [85, 90, 78, 88, 95]
total = student.total_marks(marks)
percent = student.percentage(marks, 100)
grade = student.grade(percent)

print("Total marks:", total)
print("Percentage:", percent)
print("Grade:", grade)
