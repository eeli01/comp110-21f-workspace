"""Drawing forests in a loop."""

__author__ = "730319741"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i = 1
while i <= depth:
    j = 1
    while j <= i:
        print(TREE, end="")
        j = j + 1
    print()
    i = i + 1