"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730319741"


def test_only_evens_123() -> None:
    """Tests edge case of empty list."""
    assert only_evens([]) == []


def test_only_evens_all_evens() -> None:
    """Tests when the list contains all even numbers."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]
     

def test_only_evens_mixed_list() -> None: 
    """Test when the list contains both odds and evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_sub_empty_list() -> None:
    """Tests edge case that results in an empty list."""
    assert sub([10, 20, 30], 5, 3) == []


def test_sub_first_and_last_numbers() -> None:
    """Tests to give back first and last numbers of list."""
    assert sub([10, 20, 30, 40], 0, 4) == [10, 40]


def test_sub_middle_numbers() -> None:
    """Tests to give back the numbers in middle of list."""
    assert sub([10, 20, 30, 40], 2, 4) == [30, 40]


def test_concat_two_empty_lists() -> None:
    """Tests what happens if both listts are empty."""
    assert concat([], []) == []


def test_concat_different_lenghts() -> None:
    """Tests combining two different length lists."""
    assert concat([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]


def test_concat_same_lenghts() -> None: 
    """Tests combining two same length lists."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]