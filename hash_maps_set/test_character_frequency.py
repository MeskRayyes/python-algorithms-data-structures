
from character_frequency import character_frequency


def test_basic_frequency():
    assert character_frequency("banana") == {
        "b": 1,
        "a": 3,
        "n": 2
    }


def test_empty_string():
    assert character_frequency("") == {}


def test_single_character():
    assert character_frequency("a") == {"a": 1}


def test_all_characters_unique():
    assert character_frequency("abc") == {
        "a": 1,
        "b": 1,
        "c": 1
    }


def test_repeated_characters():
    assert character_frequency("aaaa") == {"a": 4}


def test_case_sensitivity():
    assert character_frequency("AaA") == {
        "A": 2,
        "a": 1
    }
