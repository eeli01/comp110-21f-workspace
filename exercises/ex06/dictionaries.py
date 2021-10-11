"""Practice with dictionaries."""

__author__ = "730319741"

# Define your functions below


def invert(original: dict[str, str]) -> dict[str, str]:
    """Create new dictionary that switches the key-value pairs of the original dictionary."""
    invert_original = {}
    for key, value in original.items():
        if value in invert_original.keys():
            raise KeyError("There is a duplicate value in dictionary.")
        invert_original[value] = key
    return invert_original
    
    
def favorite_color(favorites: dict[str, str]) -> str: 
    """Given a dictionary of names and colors, print the color that is repeated the most times."""
    # make empty dictionary
    count = {}
    # loop through original dictionary
    # each time new color seen add it to empty dictionary
    for color in favorites.values():
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    # create list of keys of new dictionary
    k_list: list[str] = list(count.keys())
    # create list of values of new dictionary
    v_list: list[int] = list(count.values())
    # find largest in list of values
    m = max(v_list)
    k_index = v_list.index(m)
    # return original dictionary value from the key in second dictionary with largest count
    return k_list[k_index]


def count(a_list: list[str]) -> dict[str, int]:
    result = {}
    for item in a_list:
        if item in result.keys():
            result[item] += 1
        else:
            result[item] = 1
    return result
    