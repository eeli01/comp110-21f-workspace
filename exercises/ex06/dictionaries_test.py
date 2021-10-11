"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730319741"


def test_invert_duplicate_keys() -> None: 
    """Tests edge case when there are duplicate keys in key-value pair."""
    assert invert({"a": "apple", "b": "apple"}) == KeyError("There is a duplicate value in dictionary.")


def test_invert_one_pair() -> None:
    """Tests use case with one key-value pair."""
    assert invert({"a": "1"}) == {'1': 'a'}


def test_invert_multiple_pairs() -> None:
    """Tests use case with multiple key-value pairs."""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


def test_favorite_color_one_color() -> None:
    """Tests edge case with four key-value pairs but two colors repeated."""
    assert favorite_color({"eli": "blue", "emily": "yellow", "bri": "blue", "hannah": "yellow"}) == "blue"


def test_favorite_color_three_pair_two_color() -> None:
    """Tests use case where three key-value pairs are present but one color repeated."""
    assert favorite_color({"eli": "blue", "emily": "yellow", "bri": "blue"}) == "blue"


def test_favorite_color_four_pair_two_color() -> None:
    """Tests use case with four key-value pairs with one duplicate color"""
    assert favorite_color({"eli": "blue", "emily": "yellow", "bri": "yellow", "hannah": "yellow"}) == "yellow"


def test_count_empty_list() -> None:
    """Tests edge case if given empty list."""
    assert count([]) == {}


def test_count_no_duplicates() -> None:
    """Test use case when list has one index."""
    assert count(["a"]) == {"a": 1}


def test_count_duplicates() -> None:
    """Test use case when list has duplicates."""
    assert count(["a", "b", "a", "c"]) == {"a": 2, "b": 1, "c": 1}