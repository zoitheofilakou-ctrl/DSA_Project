### Binary Search Tree Analysis

**Data Structure:** Binary Search Tree (BST)  
**Scenario:** Sales Value Management  
**Source File:** data_structures/bst_tree.py  

---

### Description

A Binary Search Tree (BST) organizes numeric data in a hierarchical structure that enables fast searching and sorting.  
Each node contains a value and two branches: the left holds smaller values and the right holds larger ones.  
In this project, the BST is used to store sales figures, allowing new values to be added dynamically and displayed in sorted order using in-order traversal.  
This makes it efficient for managing datasets that must stay ordered while supporting frequent insertions and lookups.

---

### Implementation Summary

The implementation includes two main components:  

- **Node** – stores an individual value with references to left and right child nodes.  
- **SalesBSTree** – manages the root and provides core operations:  
  - `insert(value)` – adds a new sales value in the correct place.  
  - `search(value)` – checks if a specific value exists.  
  - `inorder_display(node)` – displays all values in ascending order.  

Each function is implemented recursively, which keeps the code simple and demonstrates the natural recursive structure of binary trees.

---

### Testing and Validation

Testing was carried out with the **pytest** framework in `tests/test_bst_tree.py`.  
The tests verified insertion order, search results, and traversal output.  
All cases passed successfully, confirming that the BST correctly follows its left-right ordering rule and returns values in sorted order when traversed.

---

### Time and Space Complexity

- **Insert:** O(log n) average, O(n) worst (unbalanced tree)  
- **Search:** O(log n) average, O(n) worst  
- **Traversal:** O(n)  
- **Space:** O(n), proportional to number of nodes  

Performance is efficient for balanced trees but can degrade if data is inserted in sorted order.

---

### Debugging Notes

A missing argument in the recursive search call was fixed by adding the value parameter to each recursive step.  
All tests were rerun successfully after the correction.  
Imports were also verified to work correctly from the project root.

---

### Conclusion

The Binary Search Tree offers fast, structured access to data and serves as the foundation for more advanced trees like AVL or Red-Black Trees.  
Its simple recursive design makes it ideal for learning how hierarchical data is organized and accessed.  
This module continues the same workflow as previous structures — implementation, testing, debugging, and integration into the main program — while introducing efficient hierarchical searching.
