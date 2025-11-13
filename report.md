# Data Structures and Algorithms Project – Documentation Report

## 1. Introduction

This project demonstrates the implementation, testing, and analysis of core **data structures** and **algorithms** using Python.  
It was developed as part of the Data Structures and Algorithms course to provide practical understanding of how different structures store and manage data, and how algorithms operate on them efficiently.

The project includes implementations of arrays, linked lists, stacks, queues, trees, and hash tables,  
as well as sorting, searching, and tree traversal algorithms.  
Each component is tested and analyzed to evaluate performance and efficiency.

---

## 2. Project Structure

The project is organized into several folders for clarity and modularity:
````
DSA_Project/
│
├── algorithms/
├── data_structures/
├── tests/
├── analysis/
├── docs/
│   ├── report.md
│   └── slides.pptx
│
├── main.py
├── README.md
└── requirements.txt
````


Each folder includes logically separated code files for better readability, testing, and maintainability.

---

## 3. Implemented Data Structures

### 3.1 Arrays / Lists
Used for storing weekly temperature data and performing operations such as access, replacement, append, and removal.  
Demonstrates constant-time access (O(1)) and linear-time aggregations (O(n)).

### 3.2 Linked List
Represents a music playlist.  
Supports adding and removing songs dynamically.  
Useful for data that changes frequently because nodes can be added or deleted efficiently.

### 3.3 Stack and Queue
**Stack:** Implements browser history (Last-In-First-Out).  
Allows push, pop, and peek operations in O(1) time.  
**Queue:** Models a customer service line (First-In-First-Out).  
Supports adding and serving clients sequentially.

### 3.4 Hash Table
Implements an email registry using a simple hash function with chaining to handle collisions.  
Provides near-constant time for insertion and lookup (O(1) on average).

### 3.5 Trees
Binary Tree, Binary Search Tree (BST), and AVL Tree structures implemented.  
Used for decision-making examples and student record management (balanced tree).  
Traversal methods (in-order, pre-order, post-order) applied for exploring or processing data.

---

## 4. Implemented Algorithms

### 4.1 Sorting
Bubble Sort, Insertion Sort, and Merge Sort were implemented and compared.  
Bubble Sort is simple but slow (O(n²)), Insertion Sort is efficient for small or nearly sorted lists,  
and Merge Sort is the fastest for large datasets (O(n log n)).

### 4.2 Searching
Linear and Binary Search algorithms were tested.  
Linear Search checks each element one by one (O(n)),  
while Binary Search works only on sorted data and is much faster (O(log n)).

### 4.3 Tree Traversal
In-order, Pre-order, and Post-order traversals were implemented to visit all nodes in different sequences.  
Each method has linear time complexity (O(n)) and is used for specific purposes such as sorting, copying, or deleting tree data.

---

## 5. Testing and Validation

Each data structure and algorithm was tested separately using corresponding files in the `/tests` folder.  
Examples include:

- `test_array_lists.py` – tests array operations and temperature analysis.  
- `test_linked_list.py` – verifies playlist creation and song removal.  
- `test_stack_queue.py` – simulates browsing and call center scenarios.  
- `test_traversal.py` – tests all three tree traversal methods on a sample tree.

All tests were executed successfully, confirming correct functionality of insertion, deletion, and traversal operations.  
Edge cases such as empty structures and repeated values were also handled.

---

## 6. Analysis and Performance Evaluation

The `/analysis` folder includes separate markdown files with detailed theoretical analysis:

- `algorithms_analysis.md` – Time and space complexity for sorting and searching.  
- `traversal_analysis.md` – Analysis of tree traversal algorithms.  
- `performance_comparison.md` – Comparative study of sorting and traversal performance.

Performance results show that:
- Merge Sort and Binary Search are the most efficient for large, sorted data.  
- Traversal algorithms scale linearly with the number of nodes.  
- Linked lists, stacks, and queues perform operations in constant time (O(1)).

---

## 7. Conclusion

This project provided a complete, hands-on understanding of fundamental data structures and algorithms.  
Each structure was implemented, tested, and analyzed in terms of time and space complexity.  
The results show that the best choice of data structure or algorithm depends on the type and size of data.

The project successfully covers:
- Design and implementation of core data structures.  
- Testing and validation with real examples.  
- Performance and complexity analysis across multiple algorithms.

Future improvements could include implementing graphs, priority queues, and more advanced searching or sorting techniques.

---

**Author:**  
Zoi Theofilakou  
Turku University of Applied Sciences – ICT Studies  
Fall Semester 2025
