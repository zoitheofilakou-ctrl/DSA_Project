## Linked List Analysis

Data Structure: Linked List
Scenario: Music Playlist
Source File: data_structures/linked_list.py

### Description

The Linked List is a dynamic linear data structure that links elements by using pointers instead of storing them in continuous memory locations.
Those elements are named nodes, each one is composed of two parts — the data (a song title) and a pointer to the next node.

This design allows the Linked List to expand or shrink easily, without having to move or resize existing elements in memory.
It is useful in situations where the number of elements changes frequently, such as playlists, queues, or undo/redo operations.

In this project, the Linked List is a music playlist, where:

new songs can be added to the end of the list,

the first song can be removed when played or skipped,

and the user can display all songs in the order they were added.

### Implementation Summary

The implementation consists of two main classes:

**Node** – defines the basic element of the list. It contains the data (song title) and a pointer to the next node.

**LinkedList** – manages the entire playlist through a single reference, called head, which always points to the first node.

The LinkedList class includes the operations below:

- add(data) – adds a new song at the end of the list.

- remove_first() – removes the first song by moving the head pointer to the next node.

- display() – prints all songs sequentially from the first to the last.

All operations are implemented manually without using Python’s built-in list type, showing how pointer-based structures work in practice.

### Testing and Validation

Testing was carried out using the pytest framework in the file tests/test_linked_list.py.
Each test checks the logical correctness of the linked list operations rather than its printed output.
Assertions (assert statements) are used to verify that the list behaves as expected after each operation.

The following scenarios were tested:

- Adding multiple songs links the nodes in the correct order.

- Removing the first song correctly updates the head pointer.

- Removing from an empty list does not raise an error.

- Adding a song after removal works correctly.

All tests passed successfully, confirming that the structure operates correctly in all normal and boundary cases.

### Execution

The Linked List demo can be executed through the main.py file, which contains the demo_linked_list() function.
Running:

python main.py


demonstrates the structure’s main functionalities (create, add, remove, and display).
This allows users to observe the changes step-by-step directly in the terminal.

### Time and Space Complexity

Adding a new node at the end of the list requires O(n) time, since the algorithm must traverse all existing nodes to reach the last one.
Removing the first node takes O(1) time, as only the head pointer changes.
Displaying all nodes requires O(n) time because every node must be visited once.

Each operation requires constant extra space O(1), except for the total number of nodes, which occupies O(n) memory overall due to the storage of pointers.

In summary, Linked Lists trade fast element access for flexibility in insertion and deletion.
They are slower for direct access compared to arrays but more efficient when elements are frequently added or removed.

### Debugging Notes

During testing, a few small issues were encountered and resolved:


- ModuleNotFoundError: occurred when pytest was executed from inside the tests/ folder. Running it from the project root solved the problem.

- Terminal freeze: appeared during unrelated tree traversal testing and was fixed by terminating the process with Ctrl + C.

### Conclusion

The Linked List provides a flexible and dynamic approach for managing data collections whose size frequently changes.
Although it offers slower element access compared to arrays, it allows fast and efficient insertion or deletion operations.

This module completes the second stage of the Data Structures and Algorithms project, demonstrating the same development process followed in the ArrayList module:
implementation, testing, debugging, validation, and integration into the main program.