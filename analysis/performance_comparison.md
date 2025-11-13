
# Performance Analysis Report
### Data Structures & Algorithms — Python Implementation  
### Student: Zoi Theofilakou  
### Semester: Fall 2025  
---

## 1. Introduction

This report analyzes the **performance** of key algorithms implemented in Python:

### ✔ Sorting Algorithms
- Bubble Sort  
- Insertion Sort  
- Merge Sort  

### ✔ Tree Traversal Algorithms
- In-order Traversal  
- Pre-order Traversal  
- Post-order Traversal  

The goal is to measure how execution time changes as **input size increases**, and to compare the efficiency of different algorithmic approaches.

All measurements were executed using the script:

python -m analysis.performance_comparison

ruby
Copy code

---

# 2. Sorting Algorithms Performance

## 2.1 Execution Time Results

Below are the measured times for input sizes **100**, **500**, and **1000**:

### **Bubble Sort – O(n²)**  
Very slow for large inputs.

### **Insertion Sort – O(n²)**  
Still quadratic, but faster than Bubble.

### **Merge Sort – O(n log n)**  
Fast and scalable.

---

## 2.2 Measured Runtime Table

### 🔍 *Actual execution results from the script*:

| Input Size | Bubble Sort (s) | Insertion Sort (s) | Merge Sort (s) |
|-----------:|----------------:|-------------------:|----------------:|
| **100**    | 0.01869         | 0.00101            | 0.00013         |
| **500**    | 1.71282         | 0.01826            | 0.00072         |
| **1000**   | 13.78135        | 0.07482            | 0.00152         |

---

## 2.3 Interpretation

### 🟥 Bubble Sort (Slowest)
- Time grows dramatically with larger lists.
- From **0.018s → 14s**, an increase ×760!
- Inefficient for real applications.

### 🟧 Insertion Sort
- Still O(n²), but ~200× faster than Bubble.
- Good for small or nearly-sorted datasets.

### 🟩 Merge Sort (Fastest)
- Almost unaffected by large input.
- Scales efficiently due to divide-and-conquer strategy.

---

# 3. Tree Traversal Performance

Tree traversals are **O(n)** algorithms.

## 3.1 Measured Runtime Table

| Nodes | In-order (s) | Pre-order (s) | Post-order (s) |
|------:|--------------:|---------------:|----------------:|
| **50**  | 0.00002 | 0.00002 | 0.00002 |
| **100** | 0.00004 | 0.00003 | 0.00003 |
| **200** | 0.00010 | 0.00006 | 0.00006 |
| **500** | 0.00016 | 0.00014 | 0.00015 |

---

## 3.2 Interpretation

### 🌳 Traversal Observations:
- All three traversal algorithms have **similar performance**.
- Runtime increases **linearly** with the number of nodes.
- Differences between them are tiny because:
  - All perform one full visit of the tree.
  - No complex operations are involved.

### 📌 Conclusion:
Tree traversal algorithms are **efficient**, consistent, and scale very well.

---

# 4. Overall Comparison Summary

### 📌 Sorting Summary
- **Merge Sort is by far the most efficient**.
- **Insertion Sort** is acceptable for small lists.
- **Bubble Sort is impractical** for medium/large input sizes.

### 📌 Traversal Summary
- All traversal types (in-order, pre-order, post-order) scale smoothly.
- Performance remains stable even at 500+ nodes.
- No significant difference between traversal types.

---

# 5. How to Reproduce the Results

### ▶ Run the performance comparison script:

python -m analysis.performance_comparison

shell
Copy code

### The output includes:
- Sorting runtime results  
- Tree traversal runtime results  

### The code is located at:
analysis/performance_comparison.py

shell
Copy code

### Sorting and traversal functions are implemented in:
algorithms/sorting.py
algorithms/traversal.py
data_structures/bst_tree.py

yaml
Copy code

---

# 6. Conclusion

This performance study demonstrates the clear difference between **quadratic algorithms (O(n²))** and **efficient divide-and-conquer algorithms (O(n log n))**.

Merge Sort proves to be optimal and scalable, while Bubble Sort becomes unusable beyond small inputs.

Tree traversal algorithms are fast, predictable, and ideal for structured data such as Binary Search Trees.

This analysis forms the foundation for understanding algorithmic complexity and choosing appropriate data structures and methods in real-world applications.

---

# 7. Appendix
### Additional Notes for the Instructor
- Sorting prints are fully suppressed to ensure reliable timing.
- Traversal functions use `SalesBSTree` to generate balanced/random BSTs.
- All tests pass correctly (`test_traversal.py`, `test_sorting.py`, etc.)
