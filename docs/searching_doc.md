### Searching Algorithms Analysis

**Algorithms:** Linear Search, Binary Search  
**Scenario:** Movie Titles and Student ID Lookup  
**Source File:** algorithms/searching.py  

---

### Description

This module introduces two essential searching algorithms — **Linear Search** and **Binary Search** — used to locate specific elements within datasets.  
Each algorithm demonstrates a different approach to finding a target value, showing how data order affects efficiency.

- **Linear Search** performs a simple sequential check across all items.  
- **Binary Search** divides a sorted dataset into halves, drastically reducing the number of comparisons needed.

The goal of this module is to compare both methods in terms of logic, performance, and suitability for different data conditions.

---

### Implementation Summary

- **linear_search(arr, target)** – iterates through the list one element at a time until it finds the target or reaches the end.  
  - Works on **unsorted** lists.  
  - Returns the **index** of the target if found, otherwise `-1`.  
  - Example use: searching for a movie title in an unordered list.

- **binary_search(arr, target)** – repeatedly divides the sorted list in half, comparing the target to the middle element.  
  - Requires the list to be **sorted**.  
  - Returns the **index** of the target if found, otherwise `-1`.  
  - Example use: searching for a student ID in a sorted registry.

Each function includes print statements for demonstration, showing how comparisons progress during execution.

---

### Testing and Validation

Testing was conducted using **pytest** in `tests/test_searching.py`.  
Both algorithms were tested with multiple cases to ensure accuracy and robustness:

- **Linear Search Tests:**
  - Target found in the middle of the list.  
  - Target not found.  
  - Empty list case.  
  - Target as the first or last element.

- **Binary Search Tests:**
  - Target present in a sorted list.  
  - Target not found.  
  - Target as first or last element in the list.

All test cases passed successfully, confirming correct logic for both algorithms and proper handling of edge cases.

---

### Expected Search Outcomes

| Algorithm | Dataset Example | Target | Expected Result |
|------------|----------------|---------|----------------|
| **Linear Search** | `["Interstellar", "The Godfather", "Inception", "Titanic", "Gladiator"]` | `"Titanic"` | Found at index **3** |
| **Linear Search** | `["Interstellar", "The Godfather", "Inception"]` | `"Avatar"` | Not found → **-1** |
| **Binary Search** | `[101, 105, 112, 120, 134, 150, 160]` | `120` | Found at index **3** |
| **Binary Search** | `[101, 105, 112, 120, 134, 150, 160]` | `130` | Not found → **-1** |

These results were verified both visually (via demo output) and automatically through pytest assertions.

---

### Time and Space Complexity

**Linear Search**  
- **Best case:** O(1) — when the target is the first element.  
- **Average / Worst case:** O(n) — may check every element.  
- **Space complexity:** O(1) — requires no additional memory.  
- Simple and universal, but inefficient for large datasets.

**Binary Search**  
- **Best / Average / Worst case:** O(log n) — halves the search interval each step.  
- **Space complexity:** O(1) for iterative implementation.  
- Extremely efficient on sorted data but requires pre-sorted input.  

Binary Search is exponentially faster than Linear Search for large datasets, but not usable on unsorted data.

---

### Debugging Notes

Initial test runs worked as expected for **Linear Search**, but Binary Search required additional verification to ensure correct handling of `low`, `high`, and `mid` boundaries.  
Extra print statements were added to show comparison steps and confirm the logic visually.  
Finally, all debug prints were retained for educational purposes.  

Both search functions were successfully imported and tested after adding `__init__.py` files to the project folders to ensure pytest recognized all modules.

---

### Conclusion

This module demonstrates how search performance depends on dataset organization and algorithm design.  

- **Linear Search** is the most general method — it works on any list but scales poorly.  
- **Binary Search** offers exceptional speed but only applies to **sorted data**.  

Together, these two algorithms illustrate the fundamental trade-off between **simplicity** and **efficiency**, forming the foundation for more advanced search techniques such as hash-based or tree-based lookup methods.
