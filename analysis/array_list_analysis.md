# Array / List Analysis

Data Structure: Python List (Array Example)
Scenario: Weekly Temperature Tracking
Source File: data_structures/arrays_lists.py

---

## Description

This structure shows how Python lists can be used to record and change a small number of values, 
like daily temperatures in one week.  
The function week_temp() does simple list actions such as reading, changing, adding, 
and removing elements, and also finds the mean, minimum and maximum temperature.

## Time and Space Complexity

The operations in the list have the following complexity:

- **Accessing an element** (temperatures[i]): O(1) time and O(1) space  
  because Python lists allow direct access by index.

- **Replacing an element** (temperatures[2] = 15): O(1) time and O(1) space  
  because the value is updated directly in the same memory position.

- **Appending a new value** (temperatures.append(18.2)): O(1) on average  
  because adding at the end of a list is constant time, unless Python has to grow the list.

- **Removing the last element** (temperatures.pop()): O(1) time  
  because it just deletes the last item.

- **Finding the mean, minimum, or maximum value**: O(n) time and O(1) space  
  because the code must go through all elements once to calculate the result.

Overall:
- Most actions are O(1) — very fast and independent of list size.  
- Only calculations like sum(), min(), and max() depend on the list length → O(n).  
- Memory use is small (O(n)) and grows with the number of elements.


## Notes

- Most list operations like access, append, pop or replace are very fast → O(1).  
- Operations that need to check all items (sum, min, max) take more time → O(n).  
- Memory use is small and depends on the number of elements (O(n)).