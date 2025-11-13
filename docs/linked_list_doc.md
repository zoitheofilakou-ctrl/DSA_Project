### Linked List Analysis

**Data Structure:** Linked List  
**Scenario:** Music Playlist  
**Source File:** data_structures/linked_list.py  

---

### Description

A Linked List is a linear data structure where each element (node) stores data and a reference to the next node instead of being placed in consecutive memory locations.  
This design allows the structure to grow or shrink dynamically without needing to resize existing data.  
In this project, the Linked List models a music playlist: new songs can be added at the end, the first song can be removed when played, and the full list can be displayed in the order songs were added.  
It demonstrates how pointer-based data structures manage changing datasets more flexibly than arrays.

---

### Implementation Summary

The implementation contains two main classes:  

- **Node** – represents a single song, storing its title and a pointer to the next song.  
- **LinkedList** – manages the entire playlist through the `head` reference, which always points to the first node.  

Core operations include:  
- `add(data)` – adds a new song at the end of the list.  
- `remove_first()` – removes the first song by moving the head pointer to the next node.  
- `display()` – prints all songs in the current playlist order.  

These operations are manually implemented to demonstrate how linked nodes connect dynamically without using Python’s built-in list type.

---

### Testing and Validation

The Linked List was tested using **pytest** in `tests/test_linked_list.py`.  
Tests verified that adding multiple songs correctly linked nodes, removing the first node updated the head, and operations on an empty list did not cause errors.  
All tests passed successfully, confirming correct logic and stability across typical and edge cases.

---

### Time and Space Complexity

- **Add (end):** O(n) – must traverse all nodes to reach the end  
- **Remove (first):** O(1) – updates the head pointer only  
- **Display:** O(n) – visits each node once  
- **Space:** O(n) – one node per song  

The structure provides predictable linear space usage and quick insertions or deletions compared to arrays.

---

### Debugging Notes

Minor path errors occurred when running pytest inside the `tests/` directory.  
These were fixed by running tests from the project root to ensure proper imports.  
No logical issues were found after final revisions.

---

### Conclusion

The Linked List provides a simple yet powerful model for managing collections whose size changes frequently.  
Although slower than arrays for random access, it offers efficient insertion and deletion operations.  
This module continues the same development process as previous ones — implementation, testing, debugging, and integration — while introducing pointer-based dynamic memory management.
