def total_marks(marks_list):
    return sum(marks_list)

def percentage(marks_list, max_marks_each):
    total = total_marks(marks_list)
    max_total = max_marks_each * len(marks_list)
    return (total / max_total) * 100

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "Fail"
