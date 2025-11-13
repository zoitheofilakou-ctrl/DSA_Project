# tests/test_traversal.py
# ----------------------------------------------------------
# Tests for Tree Traversal Algorithms
# ----------------------------------------------------------
# Verifies that In-order, Pre-order, and Post-order Traversal
# functions return the correct visiting order for a small tree.
# ----------------------------------------------------------

from algorithms.traversal import Node, inorder_traversal, preorder_traversal, postorder_traversal


# ----------------------------------------------------------
# Helper function: create a sample binary tree
#         A
#        / \
#       B   C
#      / \
#     D   E
# ----------------------------------------------------------
def create_sample_tree():
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    return root


# ----------------------------------------------------------
# In-order Traversal (Left → Root → Right)
# ----------------------------------------------------------
def test_inorder_traversal():
    root = create_sample_tree()
    result = inorder_traversal(root)
    expected = ["D", "B", "E", "A", "C"]
    assert result == expected, "In-order traversal failed"


# ----------------------------------------------------------
#  Pre-order Traversal (Root → Left → Right)
# ----------------------------------------------------------
def test_preorder_traversal():
    root = create_sample_tree()
    result = preorder_traversal(root)
    expected = ["A", "B", "D", "E", "C"]
    assert result == expected, " Pre-order traversal failed"


# ----------------------------------------------------------
#  Post-order Traversal (Left → Right → Root)
# ----------------------------------------------------------
def test_postorder_traversal():
    root = create_sample_tree()
    result = postorder_traversal(root)
    expected = ["D", "E", "B", "C", "A"]
    assert result == expected, "Post-order traversal failed"
