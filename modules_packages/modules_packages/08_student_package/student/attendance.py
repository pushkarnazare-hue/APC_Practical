def is_eligible(attended, total, required_percent=75):
    percent = (attended / total) * 100
    return percent >= required_percent
