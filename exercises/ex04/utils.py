"""List utility functions."""

__author__ = "730319741"


# TODO: Implement your functions here.
# define function named all
# give list of int and a single int, test if int is equal to all ints in the list
# if list only has given int, result true; otherwise result false
def all(all: list[int], given: int) -> bool:
    """Return True if all int in list match given int, otherwise print False."""
    i: int = 0
    if len(all) == 0:
        return False
    # loop through each index in list
    while i < len(all):
        # test if item stored == given int
        if all[i] != given:
            # if not, return false
            return False
        i += 1
    # return true after testing entire list
    return True


# define 2 separate lists, test if every int is equal
# if equal return true, otherwise return false
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True if two strings match all indexes, otherwise print False."""
    lc_1: int = 0
    lc_2: int = 0
    while lc_1 <= len(list_1):
        if len(list_1) == 0 and len(list_2) == 0:
            return True
        else:
            if len(list_1) == 0:
                return False
            else:
                if len(list_2) == 0:
                    return False
                else:
                    if len(list_1) != len(list_2):
                        return False
                    else: 
                        if list_1[0] != list_2[0]:
                            return False
                        lc_1 += 1
    lc_2 += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest int in a list."""
    # create loop to go through each index
    max_value: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
        # if list is empty, raise a ValueError
    for largest in input:
        if largest > max_value:
            max_value = largest
    return max_value