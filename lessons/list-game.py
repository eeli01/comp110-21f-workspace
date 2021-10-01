"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# remove item from list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum values of roles
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # access an individual item
# print(rolls[0])

# # access length of list
# print(len(rolls))

# # access last item of list
# print(rolls[len(rolls)-1])