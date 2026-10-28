def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return s.replace(" ", "")
