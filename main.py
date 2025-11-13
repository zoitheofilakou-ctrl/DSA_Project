# main.py
# Demonstration of all implemented Data Structures and Algorithms
# Author: Zoi Theofilakou | Turku University of Applied Sciences | Fall 2025

# ----------------------------
# Imports from packages
# ----------------------------
from data_structures.arrays_lists import DynamicArray
from data_structures.linked_list import LinkedList
from data_structures.stack_queue import Stack, CallCenterQueue
from data_structures.hash_table import EmailRegistry
from data_structures.binary_tree import SalesAnalysisTree
from data_structures.bst_tree import SalesBSTree
from data_structures.avl_tree import insert, search, inorder
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort
from algorithms.searching import linear_search, binary_search
from algorithms.traversal import Node, inorder_traversal, preorder_traversal, postorder_traversal


# ----------------------------
# Demo
# ----------------------------
# ----------------------------
# Demo: Dynamic Array
# ----------------------------
def demo_arrays():
    print("\n--- Dynamic Array Demo ---")

    # Create an instance of DynamicArray
    arr = DynamicArray()

    # Display all elements
    print("Initial weekly temperatures:", arr.display())

    # Calculate and show the average temperature
    avg = arr.mean()
    print("Average weekly temperature:", round(avg, 1))

    # Access a specific element (e.g., Wednesday)
    print("Temperature on index 3 (Wednesday):", arr.get(3))

    # Update a specific temperature value
    arr.update(2, 15.0)
    print("Updated temperatures:", arr.display())

    # Remove the last element
    removed = arr.remove_last()
    print(f"Removed last temperature: {removed}")
    print("After removal:", arr.display())

    # Append a new temperature at the end
    arr.append(18.2)
    print("After adding a new temperature:", arr.display())

    print("\nDynamic Array demo completed successfully.")

# --------------------------------------------------------------------------

def demo_linked_list():
    print("\n=== Linked List Demo: Songs Playlist ===")

    # Create an empty linked list
    playlist = LinkedList()
    print("Step 1: Empty playlist created.")
    playlist.display()

    # Add songs
    print("\nStep 2: Adding songs...")
    playlist.add("Imagine")
    playlist.add("Black Sabbath")
    playlist.add("Hotel California")
    playlist.display()

    # Remove the first song
    print("\nStep 3: Removing the first song...")
    playlist.remove_first()
    playlist.display()

    # 4️Add a new song
    print("\nStep 4: Adding a new song...")
    playlist.add("Let it be")
    playlist.display()

    print("\nLinked List demo completed successfully!\n")


# --------------------------------------------------------------------------


def demo_stack_queue():
    print("\n--- Stack Demo (Browser History) ---")
    stack = Stack()
    stack.push("github.com")
    stack.push("spotify.com")
    stack.push("google.com")
    stack.push("kivuton.fi")
    stack.display()
    stack.pop()
    print("Current page:", stack.peek())
    stack.display()

    print("\n--- Queue Demo (Call Center) ---")
    queue = CallCenterQueue()
    queue.add_customer("George")
    queue.add_customer("Elisavet")
    queue.add_customer("Nikos")
    queue.add_customer("Irini")
    queue.display_queue()
    queue.current_customer()
    queue.next_customer()
    queue.display_queue()

# --------------------------------------------------------------------------




# --------------------------------------------------------------------------

def demo_hash_table():
    """Demonstration of a simple hash table for email registration."""
    print("\n--- Hash Table Demo: Email Registry ---")

    # Create hash table with small size to force some collisions
    registry = EmailRegistry(size=5)

    # Add emails
    registry.add_email("alice@example.com")
    registry.add_email("bob@example.com")
    registry.add_email("carol@example.com")

    # Try adding a duplicate
    registry.add_email("alice@example.com")

    # Check for an existing email
    print(f"Check if 'bob@example.com' exists → {registry.exists('bob@example.com')}")

    # Display table contents
    print("\nCurrent Hash Table State:")
    registry.display()


# --------------------------------------------------------------------------

def demo_binary_tree():
    """Demonstration of a simple binary tree used for sales analysis decisions."""
    print("\n--- Binary Tree Demo: Sales Analysis ---")
    
    # Create tree
    sales_tree = SalesAnalysisTree()

    # Display tree structure recursively
    print("Displaying Sales Analysis Decision Tree:\n")
    sales_tree.display(sales_tree.root)

    # Summary
    print("\nExplanation:")
    print("The binary tree models a decision process:")
    print("If Region = North → check Season.")
    print("If Season = Winter → Sales: High, else Sales: Moderate.")
    print("If Region ≠ North → Sales: Low.")

# --------------------------------------------------------------------------


def demo_bst_tree():
    """Demonstration of a Binary Search Tree for sorted sales values."""
    print("\n--- Binary Search Tree Demo: Sales Data ---")

    # Create the BST
    bst = SalesBSTree()

    # Insert sample sales values (unsorted)
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting sales values: {values}")
    for value in values:
        bst.insert(value)

    # Display the sorted (in-order) output
    print("\nSorted Sales (In-Order Traversal):")
    bst.inorder_display(bst.root)
    print("\n")

    # Demonstrate searching for existing and non-existing values
    targets = [40, 90]
    for target in targets:
        found = bst.search(target)
        status = "Found " if found else "Not Found "
        print(f"Search for {target}: {status}")

    print("\nExplanation:")
    print("- Smaller sales values go to the left branch.")
    print("- Larger sales values go to the right branch.")
    print("- In-order traversal prints all values in ascending order.")

# --------------------------------------------------------------------------

def demo_avl_tree():
    print("\n DEMO: Balanced AVL Tree (Students by ID)")
    print("==========================================")

    # Step : Start with an empty tree
    root = None

    # Step : Insert some students
    print("\n Inserting students...")
    students = [
        (30, "Alice"),
        (10, "Bob"),
        (40, "Charlie"),
        (5, "Diana"),
        (20, "Eve"),
        (35, "Frank"),
        (50, "Grace")
    ]

    for sid, name in students:
        print(f"Inserting {sid} - {name}")
        root = insert(root, sid, name)

    # Step : Display the tree in sorted order (inorder traversal)
    print("\n Sorted students (Inorder Traversal):")
    inorder(root)  # Will print IDs and names in ascending order

    # Step : Search for specific students
    print("\n Searching for students by ID:")
    search_ids = [20, 35, 99]  # 99 does not exist
    for sid in search_ids:
        result = search(root, sid)
        if result:
            print(f" Found: ID {sid} → {result}")
        else:
            print(f" Student with ID {sid} not found.")

    # Step : Small explanation for the console output
    print("\n NOTE:")
    print("The tree automatically performs rotations (LL, RR, LR, RL)")
    print("to stay balanced, keeping operations efficient: O(log n).")

# --------------------------------------------------------------------------

def demo_sorting():
    print("\nDEMO: Sorting Algorithms")
    print("=============================")
    
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", data)

    # Bubble Sort
    print("\nBubble Sort:")
    print("Sorted:", bubble_sort(data.copy()))

    # Insertion Sort
    print("\nInsertion Sort:")
    print("Sorted:", insertion_sort(data.copy()))

    # Merge Sort
    print("\n Merge Sort:")
    print("Sorted:", merge_sort(data.copy()))


# --------------------------------------------------------------------------

def demo_searching():
    print("\nDEMO: Searching Algorithms")
    print("==============================")

    # Linear Search
    print("\n Linear Search (Movies List)")
    movies = ["Interstellar", "The Godfather", "Inception", "Titanic", "Gladiator"]
    print("Movies:", movies)
    linear_search(movies, "Titanic")
    linear_search(movies, "Avatar")

    # Binary Search
    print("\nBinary Search (Sorted Student IDs)")
    student_ids = [101, 105, 112, 120, 134, 150, 160]
    print("Student IDs:", student_ids)
    binary_search(student_ids, 120)
    binary_search(student_ids, 130)

# --------------------------------------------------------------------------

def demo_tree_traversal():
    print("\n--- Binary Tree Traversal Demo ---")
    print("===================================")

    # Build a simple binary tree 
    #         50
    #        /  \
    #      30    70
    #     / \    / \
    #   20  40  60  80

    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    #  Perform and display each traversal
    print("\nIn-order Traversal (Left → Root → Right):")
    print(inorder_traversal(root))  # Expected: [20, 30, 40, 50, 60, 70, 80]

    print("\nPre-order Traversal (Root → Left → Right):")
    print(preorder_traversal(root))  # Expected: [50, 30, 20, 40, 70, 60, 80]

    print("\nPost-order Traversal (Left → Right → Root):")
    print(postorder_traversal(root))  # Expected: [20, 40, 30, 60, 80, 70, 50]

    print("\n Traversals completed successfully — each node visited exactly once (O(n)).")


# ----------------------------
# Main Execution
# ----------------------------
def main():
    print("=== Demonstration of Data Structures and Algorithms Project ===")
    demo_arrays()
    demo_linked_list()
    demo_stack_queue()
    demo_hash_table()
    demo_binary_tree()
    demo_bst_tree()
    demo_avl_tree()
    demo_sorting()
    demo_searching()
    demo_tree_traversal()
    print("\nAll demos completed successfully!")


if __name__ == "__main__":
    main()
