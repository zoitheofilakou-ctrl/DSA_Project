"""
Unit Tests for DynamicArray
---------------------------
This file tests all basic operations of the DynamicArray class
implemented in data_structures/arrays_lists.py.
"""

from data_structures.arrays_lists import DynamicArray


def test_initial_values():
    arr = DynamicArray()
    data = arr.get_all()
    assert isinstance(data, list)
    assert len(data) == 7  # initial 7 temperatures
    assert round(arr.mean(), 1) == round(sum(data) / len(data), 1)


def test_append_and_remove():
    arr = DynamicArray()
    arr.append(18.5)
    assert 18.5 in arr.get_all()
    removed = arr.remove_last()
    assert removed == 18.5


def test_update_and_access():
    arr = DynamicArray()
    old_value = arr.get(2)
    arr.update(2, 99.9)
    assert arr.get(2) == 99.9
    assert arr.get(2) != old_value


def test_average_and_display():
    arr = DynamicArray()
    avg = arr.mean()
    assert isinstance(avg, float)
    displayed = arr.display()
    assert isinstance(displayed, list)
    assert all(isinstance(x, (int, float)) for x in displayed)
