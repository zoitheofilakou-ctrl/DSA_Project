"""
Unit Tests for Stack and Queue
------------------------------
This file tests the basic operations of:
- Stack (LIFO)
- CallCenterQueue (FIFO)

It uses "assert" statements to automatically check 
if our code works correctly.
If an assert condition is False → the test fails.
"""

# Import the classes from our data_structures folder
from data_structures.stack_queue import Stack, CallCenterQueue


# ---------- STACK TESTS ----------

def test_stack_push_and_pop():
    # Create an empty stack
    s = Stack()

    # Add three items (A, B, C)
    s.push("A")
    s.push("B")
    s.push("C")

    # The top element should be the last one we added (LIFO rule)
    assert s.peek() == "C"

    # Remove (pop) the top element
    removed = s.pop()
    assert removed == "C"          # should remove C
    assert s.peek() == "B"         # now B should be on top

    # Remove the remaining items
    s.pop()
    s.pop()

    # The stack should now be empty
    assert s.is_empty() == True


def test_stack_empty_behavior():
    # Create an empty stack
    s = Stack()

    # It should be empty at the start
    assert s.is_empty() == True

    # If we try to pop or peek an empty stack,
    # the method returns None (nothing to show)
    assert s.pop() is None
    assert s.peek() is None



# ---------- QUEUE TESTS ----------

def test_queue_add_and_serve():
    # Create a new queue for customers
    q = CallCenterQueue()

    # Add customers (FIFO: First In First Out)
    q.add_customer("Anna")
    q.add_customer("Bob")
    q.add_customer("Chris")

    # The first added customer (Anna) should be served first
    first = q.current_customer()
    assert first == "Anna"

    # Now the next in line should be Bob
    assert q.next_customer() == "Bob"


def test_queue_empty_behavior():
    # Create an empty queue
    q = CallCenterQueue()

    # It should start empty
    assert q.is_empty() == True

    # If we try to serve or check the next customer in an empty queue,
    # the method returns None (no one is waiting)
    assert q.current_customer() is None
    assert q.next_customer() is None
