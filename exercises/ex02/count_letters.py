"""Counting letters in a string."""

__author__ = "730319741"

letter_give: str = input("What letter do you want to search for?: ") 
word: str = input("Enter a word: ")
i: int = 0
list: str = word
count: int = 0

while i < len(list):
    if list[i] == letter_give:
        count = count + 1
    i = i + 1
print("Count: " + str(count))