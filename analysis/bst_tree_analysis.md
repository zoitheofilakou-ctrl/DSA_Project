# Binary Search Tree Analysis

Data Structure: Binary Search Tree (BST)  
Scenario: Sales Value Management  
Source File: data_structures/bst_tree.py

---

## Description

A Binary Search Tree organizes elements in a way that allows
fast searching, inserting, and sorting.

Each node follows the rule:
- Left child < Parent
- Right child > Parent

In my example, sales numbers are stored in a BST.
When displayed using in-order traversal, the sales appear in **sorted order**.

---

## Time and Space Complexity

- **Insert value** → O(log n) average, O(n) worst case (if tree is unbalanced)  
- **Search value** → O(log n) average, O(n) worst case  
- **In-order traversal** → O(n) (visits all nodes once)  
- **Space** → O(n) (one node per element)

---

## Notes

- BST provides faster search than a normal list, if balanced.  
- If the tree becomes unbalanced (e.g., inserting sorted data),  
  performance may degrade to O(n).  
- Space usage grows linearly with the number of nodes.

---

## Performance Observation

Inserting and displaying 7 sales values was instant.
The output appeared sorted, confirming that the in-order traversal works correctly.
The performance fits the expected O(log n) average behavior for BSTs.
Adding more values may lead to unbalanced trees, which could slow down operations.