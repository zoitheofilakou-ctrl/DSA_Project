# Goal: Verify that all AVL Tree operations (insert, search, inorder)
# work correctly and that the tree stays balanced after insertions.
#
# We use pytest to automatically test each function.
# To run these tests from the project root:
#     pytest tests/test_avl_tree.py -v
# ----------------------------------------------------------

import pytest
from data_structures.avl_tree import (
    StudentNode, insert, search, inorder, get_balance, get_height
)


# -----------------------------------------------------------------
# Helper function to collect the output of inorder() into a list
# instead of printing it to the screen.
# It returns a list of tuples: (student_id, student_name)
# -----------------------------------------------------------------
def collect_inorder(root):
    result = []

    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append((node.student_id, node.name))
            _inorder(node.right)

    _inorder(root)
    return result


# ----------------------------------------------------------
# Test : Insert a single student node
# ----------------------------------------------------------
def test_single_insertion():
    root = None  # Start with an empty tree
    root = insert(root, 10, "Alice")  # Insert the first student

    # Check that the node was created correctly
    assert root.student_id == 10
    assert root.name == "Alice"

    # A single node has a height of 1
    assert get_height(root) == 1

    # Balance factor should be 0 (no imbalance)
    assert get_balance(root) == 0


# ----------------------------------------------------------
# Test : Multiple insertions and tree rotations (LL, RR)
# ----------------------------------------------------------
def test_multiple_insertion_balancing():
    root = None
    # Insert nodes in decreasing order -> triggers LL rotation
    root = insert(root, 30, "A")
    root = insert(root, 20, "B")
    root = insert(root, 10, "C")  # This should cause a right rotation

    # After balancing, the root should now be 20
    assert root.student_id == 20

    # The inorder traversal must always be sorted
    assert collect_inorder(root) == [(10, "C"), (20, "B"), (30, "A")]

    # Add more nodes to trigger another rotation (RR)
    root = insert(root, 25, "D")
    root = insert(root, 40, "E")
    root = insert(root, 50, "F")  # This will cause a left rotation

    # Verify that IDs remain sorted after all insertions
    inorder_list = collect_inorder(root)
    ids = [sid for sid, _ in inorder_list]
    assert ids == sorted(ids)


# ----------------------------------------------------------
# Test : Ensure that the tree remains balanced
# ----------------------------------------------------------
def test_balance_factors():
    root = None
    root = insert(root, 10, "A")
    root = insert(root, 20, "B")
    root = insert(root, 30, "C")  # Rotation will occur here

    # After balancing, the absolute value of the balance factor <= 1
    assert abs(get_balance(root)) <= 1


# ----------------------------------------------------------
# Test : Searching for existing and missing students
# ----------------------------------------------------------
def test_search_existing_and_missing():
    root = None
    # Insert some student records
    students = [(50, "Eva"), (20, "Bob"), (70, "Chris"), (10, "Alice")]
    for sid, name in students:
        root = insert(root, sid, name)

    # Searching for existing IDs
    assert search(root, 70) == "Chris"
    assert search(root, 10) == "Alice"

    # Searching for a non-existing ID should return None
    assert search(root, 99) is None


# ----------------------------------------------------------
# Test : Check that inorder() prints students in sorted order
# ----------------------------------------------------------
def test_inorder_sorted_output(capsys):
    # Build a small AVL tree
    root = None
    data = [(15, "A"), (10, "B"), (20, "C"), (25, "D"), (5, "E")]
    for sid, name in data:
        root = insert(root, sid, name)

    # Call inorder() which prints to the terminal
    inorder(root)

    # capsys captures what was printed
    captured = capsys.readouterr()

    # Split the printed lines and clean them
    lines = [line.strip() for line in captured.out.splitlines() if line.strip()]

    # Extract just the IDs (before the dash "-")
    ids = [int(line.split(" - ")[0]) for line in lines]

    # IDs must appear in ascending order
    assert ids == sorted(ids)