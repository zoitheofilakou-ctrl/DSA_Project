### Dynamic Array (Python List) Analysis

**Data Structure:** Dynamic Array (Python List)  
**Scenario:** Weekly Temperature Tracking  
**Source File:** data_structures/arrays_lists.py  

---

### Description

The Dynamic Array is one of the most common and efficient data structures for storing sequential data.  
In Python, it is implemented as the built-in `list` type, which can automatically resize to accommodate new elements.  
In this project, the Dynamic Array stores and manages weekly temperature values, allowing easy addition, reading, updating, and removal of data.  
It provides a simple yet powerful model for handling variable-sized datasets efficiently while maintaining fast access to individual elements.

---

### Implementation Summary

The implementation defines a **DynamicArray** class with the following key methods:  

- `display()` – returns all stored temperature values.  
- `mean()` – calculates the average temperature.  
- `get(index)` – retrieves the value at a given position.  
- `update(index, new_value)` – modifies a temperature value.  
- `remove_last()` – removes and returns the last element.  
- `append(value)` – adds a new temperature to the end.  
- `get_all()` – returns the full list of elements.  

Most operations run in constant time because they directly access or modify list indices.  
Only methods that require visiting all elements, such as calculating the mean, have linear complexity.

---

### Testing and Validation

Testing was performed using the **pytest** framework in `tests/testarraylists.py`.  
Each method was tested for logical correctness using `assert` statements to compare expected and actual results.  
All tests passed successfully after removing a duplicate file and clearing cache directories.  
Testing focused on verifying internal logic rather than printed output, ensuring automated and consistent validation.

---

### Time and Space Complexity

- **Access / Update:** O(1) time, O(1) space  
- **Append / Pop:** O(1) amortized time, O(1) space  
- **Mean (aggregate operations):** O(n) time, O(1) space  
- **Overall:** O(1)–O(n) time depending on the operation, O(n) space for storage  

The structure achieves excellent average performance for most operations while maintaining linear memory usage.

---

### Debugging Notes

- **ImportError:** caused by an old duplicate function file. Fixed by deleting the outdated version.  
- **ModuleNotFoundError:** occurred when running pytest from inside the `tests/` folder. Solved by executing from the project root and adjusting the path.  
- **Cache cleanup:** PowerShell required the correct command `Remove-Item -Recurse -Force __pycache__` to clear cache folders.  

After these fixes, all tests ran successfully.

---

### Conclusion

The Dynamic Array provides a clear and practical foundation for understanding sequential data storage in Python.  
It supports fast element access and efficient resizing, making it ideal for tasks that involve frequent additions or updates.  
This module demonstrates the essential steps of implementation, testing, debugging, and validation, forming the basis for understanding more complex data structures in the project.
