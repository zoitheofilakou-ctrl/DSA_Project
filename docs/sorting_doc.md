### Sorting Algorithms Analysis

**Algorithms:** Bubble Sort, Insertion Sort, Merge Sort  
**Scenario:** Sorting Grades, Photos, and Songs  
**Source File:** algorithms/sorting.py  

---

### Description

This module demonstrates three fundamental sorting algorithms used to arrange data in ascending order.  
Each algorithm models a real-life example — sorting student grades, organizing photos by date, and arranging music albums by release year.  
The goal is to compare algorithmic efficiency and highlight the difference between simple iterative approaches and recursive divide-and-conquer methods.

---

### Implementation Summary

- **Bubble Sort** – repeatedly compares adjacent items and swaps them if out of order; simple but inefficient for large datasets.  
- **Insertion Sort** – inserts each element into its correct position relative to already sorted elements; efficient for small or nearly sorted lists.  
- **Merge Sort** – recursively divides the list into halves, sorts each half, and merges them; stable and efficient for larger datasets.

Each function accepts a list and returns a sorted version in ascending order.  
Print statements show progress for educational visibility.

---

### Testing and Validation

The module was validated using **pytest** in `tests/test_sorting.py`.  
Tests confirmed that all three algorithms correctly sort unsorted, sorted, and reverse-ordered lists.  
The results matched Python’s built-in `sorted()` function, ensuring algorithmic accuracy and reliability.

---

### Time and Space Complexity

**Bubble Sort**:

Best case: O(n) when the list is already sorted.

Average and worst case: O(n²), since every pair of elements must be compared and possibly swapped.

Space complexity: O(1), because it sorts in place without using extra memory.
Bubble Sort is conceptually simple but inefficient for large datasets.

**Insertion Sort**:

Best case: O(n) for nearly sorted lists.

Average and worst case: O(n²), due to the nested loop structure required for inserting each element into position.

Space complexity: O(1).
It performs well for small datasets or when data is already partially ordered.

**Merge Sort**:

Best, average, and worst case: O(n log n) — the divide-and-conquer strategy guarantees consistent performance across all cases.

Space complexity: O(n), as temporary arrays are used to merge sublists.
Merge Sort is ideal for large or complex datasets, offering stable and predictable performance.
---

### Debugging Notes

Minor adjustments were made to remove redundant demo code and ensure proper import paths.  
Extra print statements were retained in Bubble and Insertion Sort to visualize iteration steps for beginners.

---

### Conclusion

The three sorting algorithms highlight the trade-offs between simplicity and efficiency.  
While **Bubble Sort** and **Insertion Sort** are ideal for learning and small datasets, **Merge Sort** demonstrates scalable performance for larger inputs.  
This module completes the first step of the algorithms section, linking theoretical sorting methods to real-world use cases.
