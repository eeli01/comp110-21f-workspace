"""Finding duplicate letters in a word."""

__author__ = "730319741"

user_string: str = input("Enter a word: ")

i: int = 0
count: int = 0

while i < len(user_string):
    letter = user_string[i]
    index2 = i + 1
    while index2 < len(user_string): 
        if user_string[index2] == letter:
            count = count + 1
        index2 = index2 + 1
    i = i + 1

x = count >= 1

print("Found duplicate: " + str(x))