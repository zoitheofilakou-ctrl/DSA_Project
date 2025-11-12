# Binary Tree Analysis

Data Structure: Binary Tree  
Scenario: Sales Analysis Decision Tree  
Source File: data_structures/binary_tree.py

---

## Description

A binary tree connects elements in a parent–child relationship.
Each node can have up to two children: a left and a right one.

In this example, the binary tree represents a simple **decision system**  
for analyzing sales performance based on region and season.

Example:
- Root → checks if the region is North
- Left branch → checks if it is Winter
- Right branch → shows low sales for other regions

This structure allows the company to make quick "Yes / No" decisions.

---

## Time and Space Complexity

- **Search or traversal** → O(n), because each node may need to be visited once  
- **Insert node** → O(log n) average, O(n) worst case (if unbalanced)  
- **Delete node** → O(log n) average, O(n) worst case  
- **Display tree** → O(n)  
- **Space complexity** → O(n), where n is the number of nodes

---

## Notes

- Binary trees make it easier to represent hierarchical data (like decisions or categories).  
- Searching or visiting all nodes takes O(n) time.  
- Space grows linearly with the number of nodes.  
- Balanced trees (like AVL trees) improve search and insert time to O(log n).

---

## Performance Observation

The display of the sales tree was instant.
Even with more branches, binary trees remain efficient
for decision-based structures with simple yes/no checks.

This matches the expected O(n) traversal behavior.
