
from solution.solution_a import find_duplicate as solution_a
from solution.solution_b import find_duplicate as solution_b


def test_solution_a_finds_first_duplicate():
    assert solution_a([4, 2, 7, 2, 9, 4]) == 2


def test_solution_b_finds_first_duplicate():
    assert solution_b([4, 2, 7, 2, 9, 4]) == 2


def test_no_duplicates():
    numbers = [1, 2, 3, 4, 5]

    assert solution_a(numbers) is None
    assert solution_b(numbers) is None


def test_empty_list():
    assert solution_a([]) is None
    assert solution_b([]) is None


def test_single_element():
    assert solution_a([10]) is None
    assert solution_b([10]) is None


def test_duplicate_at_start():
    numbers = [5, 5, 3, 2]

    assert solution_a(numbers) == 5
    assert solution_b(numbers) == 5


def test_negative_numbers():
    numbers = [0, -1, 0]

    assert solution_a(numbers) == 0
    assert solution_b(numbers) == 0


def test_multiple_duplicates():
    numbers = [1, 2, 2, 1]

    assert solution_a(numbers) == 2
    assert solution_b(numbers) == 2
