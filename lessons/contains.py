"""Example of a function that processes a list."""


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))

    
# define function named contains
# we can give two arguments: a needle value we're searching for in a haystack list
def contains(needle: str, haystack: list[str]) -> bool:
    """Return true if needle is found in haystack, false otherwise."""
    # loop through each index in list
    i: int = 0
    while i < len(haystack):
        # test if item stored at index is equal to needle
        if haystack[i] == needle:
            # return true if so
            return True
        i += 1
    # return false after testing each item
    return False


# Python idiom for sttarting the main function
if __name__ == "__main__":
    main()