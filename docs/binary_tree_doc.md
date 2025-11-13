### Binary Tree Analysis

Data Structure: Binary Tree
Scenario: Sales Decision Tree
Source File: data_structures/binary_tree.py

### Description

The Binary Tree is a hierarchical data structure in which each node has at most two children, referred to as the left and right child.
It is widely used to represent data that naturally forms a hierarchy, such as organizational charts, file systems, or decision processes.

In this case, the Binary Tree is used to model a Sales Analysis Decision Tree, where each internal node represents a decision or condition (for example, Region = North?), and each leaf node represents an outcome (for example, Sales: High or Sales: Low).

The goal of this structure is to demonstrate how decision-making can be represented in a clear, structured, and recursive format.

### Implementation Summary

The file binary_tree.py contains two classes:

- Node

Represents a single element of the tree.

Stores the data and references to the left and right child nodes.

- SalesAnalysisTree

Creates and connects all nodes to form the complete decision tree.

Includes the method display(node) which recursively traverses and prints the tree in a readable hierarchical form.

The structure of the tree created is as follows:

Region = North?
├── Yes → Season = Winter?
│   ├── Yes → Sales: High
│   └── No → Sales: Moderate
└── No → Sales: Low


This structure allows the user to visualize the logical decision process step by step.

### Testing and Validation

The binary tree was tested using the pytest framework in the file tests/test_binary_tree.py.
The purpose of the tests was to confirm that all nodes were properly connected and that the recursive traversal worked correctly.

The main tests included:

- Checking if the root node exists and contains the correct data.

- Verifying that all child nodes are connected in the right order.

- Ensuring that recursive traversal visits every node exactly once.

- Confirming that all expected node values appear in the tree.

All tests passed successfully.
The testing focused on logical verification — making sure the functions work as intended — rather than printed output.

### Execution

The Binary Tree demo can be executed directly through the main.py file by calling the function:

demo_binary_tree()


Running:

python main.py


will print the decision tree structure on the screen, showing how each condition leads to a specific sales outcome.

Automated testing can also be done using:

pytest -v


to verify that all methods perform correctly.

### Time and Space Complexity

Traversal: O(n), since every node is visited once.

Search: O(log n) on average for a balanced tree, O(n) in the worst case.

Insertion and Deletion: O(log n) on average, O(n) if unbalanced.

Space: O(n), proportional to the total number of nodes.

The recursive display method specifically runs in O(n) time and uses O(h) additional space, where h is the height of the tree.

### Debugging Notes

During development and testing, the following checks and fixes were made:

- Verified that each node correctly linked to its left and right children.

- Ensured that the recursive function stopped at None to avoid infinite loops.

- Counted total nodes to confirm the full structure was connected.

- Maintained consistent import paths for running pytest from the project root.

- The tree followed the same project structure and import logic as previous modules, which prevented common import errors.

### Conclusion

The Binary Tree provides a clear example of hierarchical data representation and recursive processing.
It is an essential data structure for decision-making problems, searching, and organizing data efficiently.

In this project, the Binary Tree was used to represent sales decisions in a visual and logical form, demonstrating how complex choices can be modeled step by step.
The implementation, testing, and analysis show how hierarchical data structures differ from linear ones such as arrays or linked lists, offering new ways to organize and process information effectively.