# AVL Tree Analysis

Data Structure: AVL Tree (Balanced Binary Search Tree)  
Scenario: Student ID Organizer  
Source File: data_structures/avl_tree.py

---

## Description

An AVL Tree is a self-balancing version of a Binary Search Tree.
After each insertion, it checks the balance of the tree
and performs rotations when needed to keep it balanced.

In my example, student IDs are inserted into the tree
so that the list of students always stays sorted and balanced.

---

## Time and Space Complexity

- **Insert student** → O(log n) (tree remains balanced)  
- **Search student** → O(log n)  
- **Delete student (not implemented)** → O(log n)  
- **In-order traversal** → O(n)  
- **Space complexity** → O(n), one node per student

---

## Notes

- AVL Trees stay balanced by performing rotations (LL, RR, LR, RL).  
- This balance keeps the height small, guaranteeing O(log n) operations.  
- Space grows linearly with the number of students.  
- Even when many items are inserted, performance stays fast.

---

## Performance Observation

After inserting 5 students, the AVL Tree displayed them in sorted order instantly.
The balance was maintained automatically, confirming its O(log n) behavior.
Searching for a specific ID also completed immediately.
