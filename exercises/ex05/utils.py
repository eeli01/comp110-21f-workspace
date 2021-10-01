"""List utility functions part 2."""

__author__ = "730319741"

# Define your functions below


def only_evens(input: list[int]) -> list[int]: 
    """Return a list of all evens in a given list."""
    evens_list: list[int] = list()
    i: int = 0
    while i < len(input):
        if input[i] % 2 == 0:
            evens_list.append(input[i])
        i += 1
    return evens_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Create new list of indexes chosen from the first list."""
    b_list: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or start >= len(a_list) - 1 or end <= 0:
        b_list = []
    else: 
        b_list.append(a_list[start])
        b_list.append(a_list[end - 1])
    return b_list


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Combines two separate lists into one, second list after first."""
    c_list: list[int] = list()
    i: int = 0
    while i < len(a_list):
        c_list.append(a_list[i])
        i += 1
    i = 0
    while i < len(b_list):
        c_list.append(b_list[i])
        i += 1
    return c_list