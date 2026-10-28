from student import marks, grade, attendance

marks_list = [85, 90, 78, 88, 95]
total = marks.total_marks(marks_list)
percent = marks.percentage(marks_list, 100)
student_grade = grade.get_grade(percent)
eligible = attendance.is_eligible(70, 80)

print("Total marks:", total)
print("Percentage:", percent)
print("Grade:", student_grade)
print("Attendance eligible:", eligible)
