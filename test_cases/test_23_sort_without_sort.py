import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_basic_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_order():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_original_list_unchanged():
    numbers = [5, 2, 9, 1]
    bubble_sort(numbers)
    assert numbers == [5, 2, 9, 1]


def test_empty_list():
    assert bubble_sort([]) == []