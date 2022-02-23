# Readability according to the Coleman-Liau formula
from cs50 import get_string

text = get_string("Text: ")
letters = 0
words = 1
sentances = 0

# checking numbers of letters, words, sentances
for i in range(0, len(text)):
    if (text[i].isalpha()):
        letters += 1
    if (ord(text[i]) == 32):
        words += 1
    if ((ord(text[i]) == 46) or (ord(text[i]) == 33) or (ord(text[i]) == 63)):
        sentances += 1
print(letters, words, sentances)

# implementing the Coleman-Liau formula
L = letters * 100 / words
print(L)
S = sentances * 100 / words
print(S)
index = round(0.0588 * L - 0.296 * S - 15.8)
print(index)

# counting the grades
if (index < 1):
    print("Before Grade 1")
elif (index >= 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")
        