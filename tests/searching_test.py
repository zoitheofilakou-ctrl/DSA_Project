#--------------------------- Test Searching ----------------------------------

'''
Linear Search 
It performs basic sequential check element by element
Works for unsorted list
Handles edge cases like empty list or missing element
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from algorithms.searching import linear_search


# ------------------------------------------
# 1. BASIC TEST — target exists - element found in list -
# ------------------------------------------
def test_linear_found():
    print("\nTest 1: Element found in list")
    movies = ["Interstellar", "The Godfather", "Inception", "Titanic", "Gladiator"]
    target = "Titanic"
    result = linear_search(movies, target)
    print(f"Result: Index {result}")
    assert result == 3


# ------------------------------------------
# 2. TEST - target does not exist - element not found
# ------------------------------------------
def test_linear_not_found():
    print("\nTest 2: Element not found in list")
    movies = ["Interstellar", "The Godfather", "Inception"]
    target = "Avatar"
    result = linear_search(movies, target)
    print(f"Result: Index {result}")
    assert result == -1


# ------------------------------------------
# 3. EDGE CASE — empty list
# ------------------------------------------
def test_linear_empty_list():
    print("\nTest 3: Empty list case")
    movies = []
    target = "Titanic"
    result = linear_search(movies, target)
    print(f"Result: Index {result}")
    assert result == -1


# ------------------------------------------
# 4. EDGE CASE — target is the first element
# ------------------------------------------
def test_linear_first_element():
    print("\nTest 4: Target is first element")
    movies = ["Titanic", "Inception", "Avatar"]
    target = "Titanic"
    result = linear_search(movies, target)
    print(f"Result: Index {result}")
    assert result == 0


# ------------------------------------------
# 5. EDGE CASE — target is the last element
# ------------------------------------------
def test_linear_last_element():
    print("\nTest 5: Target is last element")
    movies = ["Inception", "Gladiator", "Titanic"]
    target = "Titanic"
    result = linear_search(movies, target)
    print(f"Result: Index {result}")
    assert result == 2


# ------------------------------------------
# RUN ALL TESTS
# ------------------------------------------
if __name__ == "__main__":
    print("===================================")
    print("Running Linear Search Test Suite")
    print("===================================")

    test_linear_found()
    test_linear_not_found()
    test_linear_empty_list()
    test_linear_first_element()
    test_linear_last_element()

    print("\nAll Linear Search tests passed successfully!")


'''Binary Search
It checks the middle element first, then decides whether to continue
searching to the left or right half of the list
'''

from algorithms.searching import binary_search

print("===================================")
print("Running Binary Search Test")
print("===================================")

def test_binary_found():
    print("\nTest 1: Binary Search - Element found in sorted list")
    student_ids = [101, 105, 112, 120, 134, 150, 160]
    target = 120
    result = binary_search(student_ids, target)
    print(f"Result: {result}\n")

def test_binary_not_found():
    print("\nTest 2: Binary Search - Element not found in sorted list")
    student_ids = [101, 105, 112, 120, 134, 150, 160]
    target = 130
    result = binary_search(student_ids, target)
    print(f"Result: {result}\n")


if __name__ == "__main__":
    print("Running Binary Search tests...")
    test_binary_found()
    test_binary_not_found()
