import sys
import os
# Allow Python to see the algorithms folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.traversal import Node, inorder_traversal, preorder_traversal, postorder_traversal


'''
The first part presents 3 traversal tree algorithms on the same tree
'''
# Create a small example tree
#         A
#        / \
#       B   C
#      / \
#     D   E
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

# Show tree visually
print("=== TREE STRUCTURE ===")
print("        A")
print("       / \\")
print("      B   C")
print("     / \\")
print("    D   E")
print("=======================\n")

# A simple function to show results for each traversal
def show_traversal(name, traversal_function):
    print(f"--- {name.upper()} TRAVERSAL ---") #show each traversal name
    result = traversal_function(root) #call the correct function
    print("Visited nodes:", result)
    print("------------------------\n")

# Run each traversal
show_traversal("In-order", inorder_traversal)
show_traversal("Pre-order", preorder_traversal)
show_traversal("Post-order", postorder_traversal)


'''
The second part each traversal is applied to a different
realistic scenario'''

'''
The second part applies each traversal algorithm
to a different, real-life example.
'''

# =======================================================
# PRE-ORDER TRAVERSAL → Example: Folder structure
# =======================================================
#  Root → Left → Right
# We visit each folder before its files or subfolders.
# This is useful when we want to copy or backup folders.

print("=== REAL-LIFE EXAMPLE 1: FOLDER STRUCTURE ===")

root_folder = Node("Main Folder")
root_folder.left = Node("Documents")
root_folder.right = Node("Pictures")
root_folder.left.left = Node("Resume.docx")
root_folder.left.right = Node("Notes.txt")
root_folder.right.left = Node("dog.jpg")
root_folder.right.right = Node("holiday.png")

print("Pre-order traversal (copy order):")
print(preorder_traversal(root_folder))
print("Explanation: We visit each folder first, then its content.\n")

# =======================================================
# IN-ORDER TRAVERSAL → Example: Sorting numbers in a BST
# =======================================================
# (Left → Root → Right) is used to get data in sorted order.
# A Binary Search Tree (BST) with numbers.
# Visiting in-order gives numbers from smallest to largest.

print("=== REAL-LIFE EXAMPLE 2: SORTING NUMBERS (BST) ===")

root_numbers = Node(8)
root_numbers.left = Node(3)
root_numbers.right = Node(10)
root_numbers.left.left = Node(1)
root_numbers.left.right = Node(6)
root_numbers.right.right = Node(14)

print("In-order traversal (sorted order):")
print(inorder_traversal(root_numbers))
print("Explanation: This is how databases or search trees return sorted data.\n")

# =======================================================
# POST-ORDER TRAVERSAL → Example: Company hierarchy
# =======================================================
# Left → Right → Root
# That means we process employees before their manager.
# This is useful when calculating salaries, deleting data, etc.

print("=== REAL-LIFE EXAMPLE 3: COMPANY HIERARCHY ===")

ceo = Node("CEO")
ceo.left = Node("Manager A")
ceo.right = Node("Manager B")
ceo.left.left = Node("Developer 1")
ceo.left.right = Node("Developer 2")
ceo.right.left = Node("Analyst")

print("Post-order traversal (bottom-up):")
print(postorder_traversal(ceo))
print("Explanation: We visit employees first, then managers, then the CEO.\n")


