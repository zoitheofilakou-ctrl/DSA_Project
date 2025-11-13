import pytest
from data_structures.bst_tree import SalesBSTree

@pytest.fixture
def bst():
    """Fixture to create a sample Binary Search Tree for testing."""
    tree = SalesBSTree()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)
    return tree


#  Test: Ensures that values are inserted correctly.
def test_insertion_structure(bst):
    """Check that left and right children follow BST property."""
    root = bst.root
    assert root.value == 50
    assert root.left.value == 30
    assert root.right.value == 70
    assert root.left.left.value == 20
    assert root.left.right.value == 40
    assert root.right.left.value == 60
    assert root.right.right.value == 80


# Test: Search for existing values.
def test_search_existing_values(bst):
    """Search should return True for values that exist."""
    for value in [50, 30, 70, 20, 40, 60, 80]:
        assert bst.search(value) is True


#  Test: Search for non-existing value.
def test_search_non_existing(bst):
    """Search should return False for values not in the tree."""
    assert bst.search(999) is False
    assert bst.search(10) is False


# Test: Verify in-order traversal order.
def test_inorder_display_order(bst):
    """In-order traversal should visit nodes in ascending order."""
    result = []

    def collect(node):
        if node:
            collect(node.left)
            result.append(node.value)
            collect(node.right)

    collect(bst.root)
    assert result == sorted([50, 30, 70, 20, 40, 60, 80])


# Test: Insert a new value and confirm placement.
def test_insert_new_value(bst):
    """After inserting a new value, it should appear in the correct place."""
    bst.insert(65)
    assert bst.search(65) is True
    # Should be right child of 60
    assert bst.root.right.left.right.value == 65
