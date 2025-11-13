import pytest
from data_structures.binary_tree import SalesAnalysisTree, Node

@pytest.fixture
def sample_tree():
    """Fixture: creates a sample SalesAnalysisTree for testing."""
    return SalesAnalysisTree()


#  Test: Ensures root node is created correctly.
def test_root_node_exists(sample_tree):
    """Root should be initialized with correct data."""
    assert sample_tree.root is not None
    assert isinstance(sample_tree.root, Node)
    assert sample_tree.root.data == "Region = North?"


#  Test: Confirms left/right child hierarchy is correct.
def test_tree_structure(sample_tree):
    """Check if child nodes are connected correctly."""
    root = sample_tree.root
    assert root.left.data == "Season = Winter?"
    assert root.right.data == "Sales : Low"
    assert root.left.left.data == "Sales: High"
    assert root.left.right.data == "Sales: Moderate"


# Test: Verifies that recursive traversal covers all 5 nodes.
def test_recursive_display_depth(sample_tree):
    """Ensure recursive depth traversal covers all nodes (5 total)."""
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    total_nodes = count_nodes(sample_tree.root)
    assert total_nodes == 5


# Test: Validates data content of all nodes.
def test_all_node_data(sample_tree):
    """Check if all node data match expected decision points."""
    values = []

    def traverse(node):
        if node is None:
            return
        values.append(node.data)
        traverse(node.left)
        traverse(node.right)

    traverse(sample_tree.root)

    expected_values = [
        "Region = North?",
        "Season = Winter?",
        "Sales: High",
        "Sales: Moderate",
        "Sales : Low"
    ]

    assert sorted(values) == sorted(expected_values)
