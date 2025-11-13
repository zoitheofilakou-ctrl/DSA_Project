import pytest
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort


def test_bubble_sort_basic():
    data = [5, 3, 8, 4, 2]
    result = bubble_sort(data.copy())
    assert result == sorted(data)


def test_insertion_sort_basic():
    data = [12, 11, 13, 5, 6]
    result = insertion_sort(data.copy())
    assert result == sorted(data)


def test_merge_sort_basic():
    data = [38, 27, 43, 3, 9, 82, 10]
    result = merge_sort(data.copy())
    assert result == sorted(data)


def test_sorted_input_remains_same():
    """Ensure that sorted input stays unchanged."""
    data = [1, 2, 3, 4, 5]
    assert bubble_sort(data.copy()) == data
    assert insertion_sort(data.copy()) == data
    assert merge_sort(data.copy()) == data


def test_reverse_input_sorts_correctly():
    """Ensure algorithms can handle reverse order lists."""
    data = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bubble_sort(data.copy()) == expected
    assert insertion_sort(data.copy()) == expected
    assert merge_sort(data.copy()) == expected