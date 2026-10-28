def total_marks(marks_list):
    return sum(marks_list)

def percentage(marks_list, max_marks_each):
    total = total_marks(marks_list)
    max_total = max_marks_each * len(marks_list)
    return (total / max_total) * 100
