# Data Structures and Algorithms in Python

This project demonstrates the implementation, testing, and performance analysis of fundamental **data structures** and **algorithms** in Python.  
It was created as part of the *Data Structures and Algorithms* course at Turku University of Applied Sciences.

---
````
## Project Structure

DSA_Project/
│
├── algorithms/ # Sorting, Searching, Traversal algorithms
├── data_structures/ # Arrays, Linked Lists, Stacks, Queues, Trees, Hash Tables
├── tests/ # Test files for each structure and algorithm
├── analysis/ # Time & Space complexity and performance reports
├── docs/ # Documentation and presentation files
└── main.py # Optional entry point
````


---

## ⚙️ Main Features

- Implementation of core **data structures**:  
  Arrays, Linked Lists, Stacks, Queues, Trees, Hash Tables.

- Implementation of key **algorithms**:  
  Sorting (Bubble, Insertion, Merge),  
  Searching (Linear, Binary),  
  Tree Traversals (In-order, Pre-order, Post-order).

- **Testing and validation** using separate test files for each module.  
- **Performance analysis** based on time and space complexity (O-notation).  
- **Comparative evaluation** of sorting and traversal algorithms.

---

## ▶️ How to Run

You can run the project in two ways:

1. Running the full demonstration (`main.py`)
2. Running the automated unit tests (`pytest`)

Both methods are shown below.

---

## ▶️ 1. Run the Full Project Demo

This runs all **data structure and algorithm demonstrations**, including:

- Dynamic Array  
- Linked List  
- Stack & Queue  
- Hash Table  
- Binary Tree  
- Binary Search Tree  
- AVL Tree  
- Sorting Algorithms  
- Searching Algorithms  
- Tree Traversals  

Run from the **project root**:

```bash
python main.py
````



## ▶️ 2. Run All Tests (Recommended)

All unit tests are inside the tests/ folder.

Run all tests from the project root:
```bash
pytest -v
````
## ▶️ 3. Run a Single Test File

Examples:
```bash
pytest tests/test_traversal.py -v
pytest tests/test_array_lists.py -v
pytest tests/test_sorting.py -v
pytest tests/test_searching.py -v
````
⚠️ Do NOT run tests from inside /tests.
Always run pytest from the project root.

## ▶️ 4. Run a Specific Test Function
pytest tests/test_traversal.py::test_inorder_traversal -v

## ▶️ 5. Project Requirements

Install required packages:
```bash
pip install -r requirements.txt
````

Required package:

pytest

✔ Summary

- python main.py → run all demos

- pytest -v → run all tests

- pytest tests/<file>.py -v → test only one module

Run everything from project root

Never run inside /tests

## 📊 PERFORMANCE ANALYSIS
The performance analysis script is located at:
analysis/performance_comparison.py


Run it with:
```bash
python -m analysis.performance_comparison
````

This script compares:

✔ Sorting Algorithms

Bubble Sort

Insertion Sort

Merge Sort

✔ Tree Traversal Algorithms

In-order

Pre-order

Post-order

The collected results and discussion are found in:

analysis/performance_report.md





## 📘 Documentation

All documentation and analysis files are located in the /docs and /analysis folders:

All theoretical and descriptive documentation is located inside:
```bash
docs/
analysis/
````

### 📌 Key Theory Files
- `analysis/algorithms_analysis.md` – Sorting & Searching complexity  
- `analysis/traversal_analysis.md` – Tree traversal theory  
- `analysis/performance_report.md` – Full performance comparison  
- `docs/report.md` – Main high-level documentation  

### 📌 Additional Notes & Explanations
You will also find **extra Markdown files** that explain and analyze:

- Arrays & Dynamic Arrays  
- Linked Lists  
- Stacks & Queues  
- Hash Tables  
- Trees, Binary Trees, BSTs, AVL Trees  

These files include step-by-step explanations, scenarios, examples,  
and implementation notes that support the project requirements.

## 🧩 Purpose and Learning Outcomes

This project was developed to:

Understand how fundamental data structures work internally.

Analyze the time and space efficiency of algorithms.

Practice writing modular and testable Python code.

Compare algorithm performance for different input sizes.

Author:
Zoi Theofilakou
Turku University of Applied Sciences – ICT Studies
Fall Semester 2025