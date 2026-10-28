from texttools import cleaning, tokenization, frequency

text = "Hello, world! Hello everyone.   Welcome to Python."

cleaned = cleaning.remove_punctuation(text)
cleaned = cleaning.remove_extra_spaces(cleaned)
tokens = tokenization.tokenize(cleaned)
freq = frequency.word_frequency(tokens)

print("Cleaned text:", cleaned)
print("Tokens:", tokens)
print("Word frequency:", freq)
