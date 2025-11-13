#--------------------------- Test Searching ----------------------------------

# This file tests the two basic searching algorithms:
# 1. Linear Search  → works on unsorted lists
# 2. Binary Search  → works on sorted lists only
#
# Goal: make sure each function finds the right element
# or correctly returns -1 when the target doesn’t exist.
#
# Run from the project root:
#     pytest tests/searching_test.py -v
# ----------------------------------------------------------

import pytest
from algorithms.searching import linear_search, binary_search


# ==========================================================
#  LINEAR SEARCH TESTS
# ==========================================================
# Linear search checks every element one by one.
# It’s simple, reliable, and works even when the list
# is not sorted.
# ==========================================================


def test_linear_found():
    """ Test case: target exists somewhere in the list."""
    movies = ["Interstellar", "The Godfather", "Inception", "Titanic", "Gladiator"]
    target = "Titanic"
    # Expected: Titanic is at index 3
    result = linear_search(movies, target)
    assert result == 3


def test_linear_not_found():
    """ Test case: target is not in the list."""
    movies = ["Interstellar", "The Godfather", "Inception"]
    target = "Avatar"
    # Expected: not found → returns -1
    result = linear_search(movies, target)
    assert result == -1


def test_linear_empty_list():
    """ Edge case: searching inside an empty list."""
    movies = []
    target = "Titanic"
    # Nothing to search → must return -1
    result = linear_search(movies, target)
    assert result == -1


def test_linear_first_element():
    """ Edge case: target is the very first element."""
    movies = ["Titanic", "Inception", "Avatar"]
    target = "Titanic"
    # Found immediately at index 0
    result = linear_search(movies, target)
    assert result == 0


def test_linear_last_element():
    """ Edge case: target is the last element in the list."""
    movies = ["Inception", "Gladiator", "Titanic"]
    target = "Titanic"
    # Found at index 2 after checking all items
    result = linear_search(movies, target)
    assert result == 2


# ==========================================================
#  BINARY SEARCH TESTS
# ==========================================================
# Binary search only works if the list is sorted.
# It repeatedly divides the list in half until it
# either finds the target or confirms it’s missing.
# ==========================================================


def test_binary_found():
    """ Test case: target exists in a sorted list."""
    student_ids = [101, 105, 112, 120, 134, 150, 160]
    target = 120
    # The target 120 is found at index 3
    result = binary_search(student_ids, target)
    assert result == 3


def test_binary_not_found():
    """ Test case: target is not present."""
    student_ids = [101, 105, 112, 120, 134, 150, 160]
    target = 130
    # Not found → returns -1
    result = binary_search(student_ids, target)
    assert result == -1


def test_binary_first_element():
    """ Edge case: target is the smallest (first) element."""
    student_ids = [10, 20, 30, 40, 50]
    target = 10
    # Found immediately at index 0
    result = binary_search(student_ids, target)
    assert result == 0


def test_binary_last_element():
    """Edge case: target is the largest (last) element."""
    student_ids = [10, 20, 30, 40, 50]
    target = 50
    # Found at the last index (4)
    result = binary_search(student_ids, target)
    assert result == 4