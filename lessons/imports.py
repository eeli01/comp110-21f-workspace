"""Examples of imports."""


from lessons import helpers
# import statement means that python stops and goes to other file to evaluate helpers
# then comes back to evaluae helpers.powerful
from lessons import helpers as hp
# import helpers using alias

# import names directly from globals of module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    print(helpers.powerful(2, 4))
    # Accessed the first import

    print(hp.THE_ANSWER)
    # Accessed alias import

    print(powerful(2, 10))
    print(THE_ANSWER)
    # Call imported function directly

    print(f"imports.py: {__name__}")
    

if __name__ == "__main__":
    main()
