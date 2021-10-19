"""Examples of functions imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    # Only evaluted if ran as module
    print(powerful(2, 16))
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


if __name__ == "__main__":
    # Python idiom: typically you would call main here
    main()
# else:
    # Typically not common to do ANYTHING in the case where module is imported
    # print("Evaluated as an imported mofule")
# evaluated first because evaluated entire helper module first before any variables or functions
# importing module means that __name__ == name of imported module