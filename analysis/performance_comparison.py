"""
Performance Comparison Script
-----------------------------
This file measures and compares the execution time of:

1. Sorting Algorithms
   - Bubble Sort
   - Insertion Sort
   - Merge Sort

2. Tree Traversal Algorithms
   - In-order
   - Pre-order
   - Post-order

Goal:
-----
To understand how fast each algorithm runs as the input size grows.
This script is part of Deliverable 5 (Performance Analysis).
"""

import time
import random
import sys
import io


# ===============================================================
# 1. SILENT IMPORT OF SORTING MODULE
# ---------------------------------------------------------------
# Your sorting.py file contains demo code that prints output
# whenever it is imported.
#
# Example prints:
#   "Swapped: [...]"
#   "Inserted: [...]"
#   "Before sorting: [...]"
#
# These prints are great for learning, but BAD for performance tests.
# To avoid showing them, we temporarily disable ALL print output
# during the import of sorting algorithms.
# ===============================================================

old_stdout = sys.stdout            # Save original stdout
sys.stdout = io.StringIO()         # Redirect prints to a "trash" buffer

from algorithms.sorting import bubble_sort, insertion_sort, merge_sort

sys.stdout = old_stdout            # Restore normal print behavior


# Import traversal functions and the BST class normally
from algorithms.traversal import (
    inorder_traversal,
    preorder_traversal,
    postorder_traversal
)
from data_structures.bst_tree import SalesBSTree



# ===============================================================
# 2. SILENT WRAPPER FOR SORTING FUNCTIONS
# ---------------------------------------------------------------
# When bubble_sort() runs, it prints "Swapped: [...]".
# When insertion_sort() runs, it prints "Inserted: [...]".
#
# We DO NOT want these prints in the timing results.
# So we disable printing ONLY during sorting calls.
# ===============================================================

def silent_call(func, data):
    """
    Runs a function while temporarily blocking all print() output.

    Parameters:
        func : function – the sorting function to run
        data : list – the list that will be sorted

    Returns:
        result of the sorting function (sorted list)
    """
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()      # Disable print()
    result = func(data)
    sys.stdout = old_stdout         # Restore print()
    return result



# ===============================================================
# 3. TIMER FUNCTIONS (MEASURE EXECUTION TIME)
# ---------------------------------------------------------------

def measure_time(func, data):
    """
    Measures the execution time of a function that takes 1 argument.
    Used for sorting algorithms.
    """
    start = time.time()
    func(data)
    return time.time() - start


def measure_time_noargs(func):
    """
    Measures execution time for functions that take NO arguments.
    Used for tree traversals.
    """
    start = time.time()
    func()
    return time.time() - start



# ===============================================================
# 4. SORTING PERFORMANCE TEST
# ---------------------------------------------------------------

def test_sorting_performance():
    """
    Measures how long Bubble Sort, Insertion Sort, and Merge Sort
    take to sort lists of different sizes.
    """
    sizes = [100, 500, 1000]   # Input sizes for performance testing

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }

    print("\n=== Sorting Performance ===")
    for size in sizes:
        # Create a list of random integers for sorting
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nInput size: {size}")

        # Measure each algorithm
        for name, algo in algorithms.items():
            # Use silent_call to avoid print spam from sorting demos
            t = measure_time(lambda x: silent_call(algo, x), arr.copy())
            print(f"{name}: {t:.5f} seconds")



# ===============================================================
# 5. TREE TRAVERSAL PERFORMANCE TEST
# ---------------------------------------------------------------

def test_traversal_performance():
    """
    Measures the time needed to traverse a Binary Search Tree
    with different numbers of nodes.
    """
    sizes = [50, 100, 200, 500]

    print("\n=== Tree Traversal Performance ===")
    for size in sizes:
        bst = SalesBSTree()

        # Build a BST of random values
        for _ in range(size):
            bst.insert(random.randint(0, 10000))

        print(f"\nNodes: {size}")

        # Measure each DFS traversal
        t1 = measure_time_noargs(lambda: inorder_traversal(bst.root))
        t2 = measure_time_noargs(lambda: preorder_traversal(bst.root))
        t3 = measure_time_noargs(lambda: postorder_traversal(bst.root))

        print(f"In-order:  {t1:.5f}s")
        print(f"Pre-order: {t2:.5f}s")
        print(f"Post-order:{t3:.5f}s")



# ===============================================================
# 6. MAIN
# ---------------------------------------------------------------

if __name__ == "__main__":
    test_sorting_performance()
    test_traversal_performance()

