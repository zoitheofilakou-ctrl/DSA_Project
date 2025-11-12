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
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort
from algorithms.searching import linear_search, binary_search
from algorithms.traversal import inorder_traversal, preorder_traversal, postorder_traversal


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


def demo_hash_table():
    print("\n--- Hash Table Demo ---")
    table = EmailRegistry(10)
    table.insert("email1", "zoi@example.com")
    table.insert("email2", "theofilakou@example.com")
    table.display()
    print("Search for email1:", table.search("email1"))


def demo_sorting():
    print("\n--- Sorting Algorithms Demo ---")
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original data:", data)
    print("Bubble Sort:", bubble_sort(data.copy()))
    print("Insertion Sort:", insertion_sort(data.copy()))
    print("Merge Sort:", merge_sort(data.copy()))


def demo_searching():
    print("\n--- Searching Algorithms Demo ---")
    numbers = [3, 9, 10, 27, 38, 43, 82]
    print("Linear Search for 27:", linear_search(numbers, 27))
    print("Binary Search for 27:", binary_search(numbers, 27))


def demo_tree_traversal():
    print("\n--- Binary Tree Traversal Demo ---")
    tree = ()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(val)
    print("In-order Traversal:", inorder_traversal(tree.root))
    print("Pre-order Traversal:", preorder_traversal(tree.root))
    print("Post-order Traversal:", postorder_traversal(tree.root))


# ----------------------------
# Main Execution
# ----------------------------
def main():
    print("=== Demonstration of Data Structures and Algorithms Project ===")
    demo_arrays()
    demo_linked_list()
    demo_stack_queue()
    demo_hash_table()
    demo_sorting()
    demo_searching()
    demo_tree_traversal()
    print("\nAll demos completed successfully!")


if __name__ == "__main__":
    main()
