### Stack and Queue Analysis

**Data Structure:** Stack (LIFO) and Queue (FIFO)  
**Scenario:** Browser History & Call Center Simulation  
**Source File:** data_structures/stack_queue.py  

---

### Description

The Stack and Queue are two fundamental linear data structures that organize data in different ways depending on how elements are added and removed.  
A **Stack** follows the *Last In, First Out (LIFO)* rule — the last item added is the first one removed, similar to the back button in a browser or an undo history in an editor.  
A **Queue** follows the *First In, First Out (FIFO)* rule — the first item added is the first one processed, much like customers waiting in line.  

In this module, both data structures are implemented in simple, real-world scenarios:  
the Stack simulates browsing history, while the Queue models a call center service line.  
They demonstrate how order of insertion and removal directly affects data behavior and efficiency.

---

### Implementation Summary

The file **stack_queue.py** defines two main classes:

- **Stack (Browser History)**  
  - `push(item)` – adds a new page to the top of the stack.  
  - `pop()` – removes and returns the most recently visited page.  
  - `peek()` – shows the current page without removing it.  
  - `is_empty()` – checks whether the stack is empty.  
  - `display()` – prints the stack from top to bottom.  

- **CallCenterQueue (Customer Queue)**  
  - `add_customer(name)` – adds a new customer to the queue.  
  - `current_customer()` – serves and removes the first customer in line.  
  - `next_customer()` – shows who is next without removing them.  
  - `display_queue()` – prints all customers in the current queue order.  
  - `is_empty()` – checks whether the queue is empty.  

The Stack uses Python’s built-in **list**, while the Queue uses **collections.deque** for efficient append and pop operations from both ends.

---

### Testing and Validation

Testing was performed using **pytest** in `tests/test_stack_queue.py`.  
Each function was tested through clear, isolated examples — such as adding, removing, and checking empty structures.  
Assertions were used to verify that all operations returned the correct logical results.  
All tests passed successfully after fixing small issues related to import paths and print formatting, confirming that both structures behave correctly in all scenarios.

---

### Time and Space Complexity

- **Push / Enqueue:** O(1)  
- **Pop / Dequeue:** O(1)  
- **Peek / Next:** O(1)  
- **Display all elements:** O(n)  
- **Space:** O(n)  

Both Stack and Queue operations run in constant time for insertions and removals since they occur at the ends of the list or deque.  
Only display operations require visiting all elements, which results in linear time complexity.

---

### Debugging Notes

- **ImportError:** Occurred when the module path was not properly detected; fixed by ensuring the `data_structures` folder was included in imports.  
- **Print formatting:** The display arrow in the queue (`-->`) was updated for clarity.  
- **Assert usage:** Clarified that `assert` checks whether a condition is true, helping identify failed tests quickly.  

After these corrections, both structures ran smoothly and passed all test cases.

---

### Conclusion

The Stack and Queue form the foundation of many algorithmic processes.  
They illustrate how data order affects program logic — whether managing browser navigation (LIFO) or handling tasks in order (FIFO).  
This module reinforces essential problem-solving concepts such as abstraction, structured thinking, and algorithmic control flow.  
It follows the same consistent workflow as previous modules: implementation, testing, debugging, and validation — building toward a deeper understanding of how data structures shape efficient program design.
