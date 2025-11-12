### Stack and Queue Analysis

Data Structure: Stack (LIFO) and Queue (FIFO)
Scenario: Browser History & Call Center Simulation
Source File: data_structures/stack_queue.py

### Description

The Stack and Queue are two fundamental data structures in computer science.
They are both linear structures, which means data is stored and accessed in a specific order — but they follow different rules:

Stack → Last In, First Out (LIFO)
The last item you add is the first one you remove, like pages in a browser history or the undo feature in an editor.

Queue → First In, First Out (FIFO)
The first item you add is the first one to be processed, just like a real waiting line at a call center.

In this module, both data structures are implemented in a simple and clear way:

The Stack is used to simulate browsing history (going “back” through pages).

The Queue represents a call center where customers are served in the order they arrive.

### Implementation Summary

The file stack_queue.py includes two main classes:

-  Stack (Browser History)

push(item) – adds a new page (top of the stack)

pop() – removes and returns the most recently visited page

peek() – shows the current page without removing it

is_empty() – checks if the stack is empty

display() – prints the stack from top to bottom

- CallCenterQueue (Customer Queue)

add_customer(name) – adds a new customer to the end of the queue

current_customer() – serves and removes the first customer in line

next_customer() – shows who is next without removing them

display_queue() – prints all customers in the current order

is_empty() – checks if the queue is empty

Both classes are implemented using Python’s built-in list (for Stack) and collections.deque (for Queue), which provide efficient operations at the ends of the list.

### Testing and Validation

All core operations were tested using the pytest framework in the file
tests/test_stack_queue.py.

Each function was tested with small, clear examples — for instance:

- Pushing and popping items from the Stack.

- Adding and serving customers in the Queue.

- Checking how both structures behave when they are empty.

- Assert statements were used to confirm that the results of operations match the expected behavior.
If something is wrong, pytest automatically shows which function failed, making debugging much easier.

All tests passed successfully after fixing minor issues like import paths and typos.

### Execution

The Stack and Queue demos can be executed directly from the main.py file.
Running:

python main.py


will show two sections:

- Browser History (Stack) — simulates visiting and going back through pages.

- Call Center (Queue) — simulates customers entering and leaving a service line.

Alternatively, you can run automated tests with:

pytest -v


to verify that all methods work correctly.

Time and Space Complexity
Operation	Stack	Queue	Time Complexity	Space Complexity
Insert (push / enqueue)	: O(1)	O(1)
Remove (pop / dequeue)	:	O(1)	O(1)
Peek / Next	:	O(1)	O(1)
Display all	:	O(n)	O(n)

Stack and Queue operations are constant time O(1), since they act on the ends of the list/deque.

Only display operations require visiting all elements, giving O(n) complexity.

Both structures store data linearly, so total space is proportional to the number of stored items → O(n).

### Debugging Notes

During testing, some typical issues were found and fixed:

- ImportError:
The file could not find the right module path.
Solved by checking that the data_structures folder is included in the project imports.

- Typos in print output:
The arrow in display_queue() ("-->") was improved to " --> " for better readability.

- Testing confusion with assert:
Initially, it was unclear what assert does.
It was explained as a simple check: if the condition is true, continue; if false, raise an error.

### Conclusion

Both Stack and Queue are  important foundational data structures.
They help beginners understand how order affects data access and processing —
whether it’s last in, first out (like a browser history) or first in, first out (like a waiting line).

The implementation, testing, and validation of these structures provided practical experience with:

- Abstract thinking about how data is organized

- Writing reusable Python classes

- Using pytest for simple, automated testing