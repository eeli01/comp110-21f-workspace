"""Function writing practice."""


def odd_and_even(a_list: list[int]) -> list[int]:
    i: int = 0
    b_list: list[int] = []

    while i < len(a_list):
        if a_list[i] % 2 == 1 and i % 2 == 0:
            b_list.append(a_list[i])
        i += 1

    return b_list
