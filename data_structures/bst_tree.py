# -------------------- Binary Search Tree (Sales Data) --------------------
# This structure organizes numeric data (sales values) in a sorted, tree-like form
# Each value is stored in a "node" that can have a left and right child.
# Smaller values go to the left side, larger values go to the right side.

# -------------------- NODE CLASS --------------------

class Node:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, value):
        # Each node stores a value (for example, a sales amount)
        self.value = value
        
        # Left child will hold smaller values (None means no child yet)
        self.left = None
        
        # Right child will hold larger values (None means no child yet)
        self.right = None


# -------------------- BINARY SEARCH TREE CLASS --------------------

class SalesBSTree:
    """Binary Search Tree for storing and displaying sales values in sorted order."""
    def __init__(self):
        # The tree starts empty, so the root is initially None
        self.root = None


    # -------------------- INSERTION --------------------
    def insert(self, value):
        """Insert a new value into the BST."""
        # If the tree is empty, create the first node as the root
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, call the recursive helper to find the right place
            self._insert_recursive(self.root, value)


    def _insert_recursive(self, current, value):
        """Helper method for recursive insertion."""
        # If the new value is smaller than the current node → go left
        if value < current.value:
            # If there is no left child, insert the new value here
            if current.left is None:
                current.left = Node(value)
            else:
                # Otherwise, continue searching down the left subtree
                self._insert_recursive(current.left, value)
        
        # If the new value is greater than the current node → go right
        elif value > current.value:
            # If there is no right child, insert it here
            if current.right is None:
                current.right = Node(value)
            else:
                # Otherwise, keep going down the right subtree
                self._insert_recursive(current.right, value)
        
        # If the value already exists, we do nothing (duplicates ignored)
        # This keeps each value unique in the tree.


    # -------------------- DISPLAY (IN-ORDER TRAVERSAL) --------------------
    def inorder_display(self, node):
        """Display all values in ascending order."""
        # This function visits nodes in the correct sorted order:
        # 1. Visit all nodes in the left subtree
        # 2. Print the current node
        # 3. Visit all nodes in the right subtree
        if node:
            self.inorder_display(node.left)
            print(node.value, end=" ")
            self.inorder_display(node.right)


    # -------------------- SEARCH --------------------
    def search(self, value):
        """Search for a value in the BST and return True if found."""
        # The public search function always starts from the root
        return self._search_recursive(self.root, value)


    def _search_recursive(self, current, value):
        # Base case: if current is None → we reached a leaf with no match
        if current is None:
            return False

        # If we found the value, return True
        if current.value == value:
            return True

        # If the target is smaller → search on the left side
        elif value < current.value:
            return self._search_recursive(current.left, value)
        
        # Otherwise, search on the right side (target is larger)
        else:
            return self._search_recursive(current.right, value)
