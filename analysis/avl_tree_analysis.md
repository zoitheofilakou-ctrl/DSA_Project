### Balanced Tree (AVL Tree) Analysis

**Data Structure:** Balanced Binary Search Tree (AVL Tree)  
**Scenario:** Student Record Organizer  
**Source File:** data_structures/avl_tree.py  

---

### Description

An **AVL Tree** is a self-balancing Binary Search Tree where the height difference between the left and right subtrees of any node (the *balance factor*) is at most 1.  
This constraint ensures that the tree remains approximately balanced, maintaining logarithmic time complexity for searching, inserting, and deleting elements.

In this project, the AVL Tree is used to organize student records by their ID numbers.  
Each student is stored as a node containing a `student_id` and `name`.  
When new students are inserted, the tree automatically performs **rotations** (LL, RR, LR, RL) to restore balance.  
This guarantees that lookups and updates remain efficient regardless of the insertion order.

---

### Implementation Summary

The implementation defines a node class and multiple helper functions:  

- **StudentNode** – represents a single student record, storing `student_id`, `name`, and pointers to its left and right children along with its current height.  
- **insert(root, student_id, name)** – recursively inserts new students into the tree while maintaining the AVL balance through rotations.  
- **search(root, student_id)** – locates a student by ID, traversing left or right subtrees based on comparisons.  
- **inorder(root)** – displays all students in ascending order by ID, verifying that the BST property is preserved.  

Auxiliary functions `get_height`, `get_balance`, `rotate_left`, and `rotate_right` support balancing logic and height maintenance after each operation.

---

### Testing and Validation

The AVL Tree was thoroughly tested using **pytest** in `tests/test_avl_tree.py`.  
Tests verified single and multiple insertions, automatic balancing through rotations, correct height and balance factor values, and proper behavior of the search and inorder functions.  
`capsys` was used to capture printed traversal output, confirming that student IDs were always displayed in sorted order.  
All test cases passed successfully, ensuring reliable functionality and balance maintenance across all scenarios.

---

### Time and Space Complexity

- **Insert:** O(log n) – tree rotations keep the height balanced  
- **Search:** O(log n) – traversal depth is logarithmic  
- **Delete:** O(log n) – rebalancing required after removal  
- **Traversal (inorder):** O(n) – visits each node once  
- **Space:** O(n) – one node per student record  

The AVL Tree maintains consistently efficient performance by automatically preventing skewed structures that occur in regular Binary Search Trees.

---

### Debugging Notes

During initial testing, balance factor calculations and height updates were verified using print-based debugging to ensure correct rotation behavior.  
No logic or import errors were found after final validation.  
Minor readability improvements were made to simplify the inorder traversal and to improve unit test clarity for beginners.

---

### Conclusion

The Balanced Binary Search Tree (AVL Tree) efficiently manages ordered datasets by maintaining strict height balance through automatic rotations.  
Its predictable **O(log n)** performance makes it ideal for applications that require frequent searches, insertions, and deletions.  
This module extends the DSA project with the concept of **self-balancing trees**, emphasizing how automatic height correction ensures scalability and stable performance in dynamic datasets.
