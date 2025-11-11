"""
Traversal Algorithms for Binary Trees
-------------------------------------
Implements three classic Depth-First Traversal algorithms:
1. In-order Traversal (Left → Root → Right)
2. Pre-order Traversal (Root → Left → Right)
3. Post-order Traversal (Left → Right → Root)

Each algorithm visits all nodes exactly once → O(n) time complexity.
"""

class Node:
    """Simple Node structure for a Binary Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------- IN-ORDER Traversal --------------------
def inorder_traversal(node):
    """In-order traversal (Left → Root → Right)."""
    result = []  # Start with an empty list
    if node:
        result += inorder_traversal(node.left) # Visit left child first
        result.append(node.data)  # Then visit the root
        result += inorder_traversal(node.right)  # Finally visit right child
    return result


# -------------------- PRE-ORDER Traversal --------------------
def preorder_traversal(node):
    """Pre-order traversal (Root → Left → Right)."""
    result = []
    if node:
        result.append(node.data)
        result += preorder_traversal(node.left)
        result += preorder_traversal(node.right)
    return result


# -------------------- POST-ORDER Traversal --------------------
def postorder_traversal(node):
    """Post-order traversal (Left → Right → Root)."""
    result = []
    if node:
        result += postorder_traversal(node.left)
        result += postorder_traversal(node.right)
        result.append(node.data)
    return result
