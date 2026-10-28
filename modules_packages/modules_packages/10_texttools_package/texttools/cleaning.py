import string

def remove_punctuation(text):
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text

def remove_extra_spaces(text):
    return " ".join(text.split())
