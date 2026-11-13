
from binary_search import binary_search


def test_target_in_middle():
    assert binary_search([2, 4, 6, 8, 10, 12, 14], 8) == 3


def test_target_at_start():
    assert binary_search([2, 4, 6, 8, 10], 2) == 0


def test_target_at_end():
    assert binary_search([2, 4, 6, 8, 10], 10) == 4


def test_target_not_found():
    assert binary_search([2, 4, 6, 8, 10], 7) == -1


def test_empty_list():
    assert binary_search([], 5) == -1


def test_single_element_found():
    assert binary_search([10], 10) == 0


def test_single_element_not_found():
    assert binary_search([10], 5) == -1


def test_negative_numbers():
    assert binary_search([-10, -5, 0, 5, 10], -5) == 1
