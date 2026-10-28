import string_utils

s = input("Enter a string: ")

print("Vowel count:", string_utils.count_vowels(s))
print("Reversed:", string_utils.reverse_string(s))
print("Palindrome:", string_utils.is_palindrome(s))
print("Word count:", string_utils.count_words(s))
print("Without spaces:", string_utils.remove_spaces(s))
