import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([7]) == 7


def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_list([-2, 5, 3]) == 6


def test_original_list_unchanged():
    numbers = [1, 2, 3, 4]
    sum_of_list(numbers)
    assert numbers == [1, 2, 3, 4]