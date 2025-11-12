Array / List Analysis

Data Structure: Dynamic Array (Python List)
Scenario: Weekly Temperature Tracking
Source File: data_structures/arrays_lists.py

Description

The Dynamic Array is one of the simplest and most effective data structures for sequential data storage.
In Python, it is implemented through the built-in list type, which can easily be resized in case of adding new elements.

In the given case, the structure is being used to store and handle weekly temperatures.
The elements indicate all the temperature of every day, and the user can add, read and update or delete values without a problem.


Implementation Summary

The DynamicArray class includes several key operations:

display() – returns all stored elements

mean() – average temperature calculation

get(index) – returns the element at a specific index

update(index, new_value) – updates a temperature at the given position

remove_last() – removes and returns the last element

append(value) – adds a new temperature at the end

get_all() – returns the complete list of elements

Most of these operations have constant time complexity because they directly access or modify list elements.
Only operations that need to examine all elements, such as calculating the mean, have linear complexity.

Testing and Validation

The pytest framework was used in the file tests/testarraylists.py to test all of the methods of the class.

The tests confirm that:

The array initializes correctly and computes the mean accurately.

Elements can be added, updated, and removed as expected.

Data types and returned values are consistent.

Every test was successful following the deletion of a duplicate file as well as clearing the cache directories (pycache).

Execution

The DynamicArray class can run either through the main.py file or by running the test file.
Running python main.py will show an example of its usage, while pytest -v will run automated validation tests.


Time and Space Complexity


Access and Update: Constant time O(1) and constant extra space O(1), because list elements can be accessed directly by index.

Append and Pop: Constant time on average O(1) amortized, Each operation requires constant extra space, although the total list size grows linearly O(n).

Mean, Min, and Max: Linear time O(n) and constant space O(1), since the algorithm must visit every element once.

Overall: Performance depends on the operation type. Time complexity ranges between O(1) and O(n), while space complexity is O(n) due to the total number of stored elements.

Debugging Notes

When testing was done, there were some problems that arose which were resolved in the following way:

ImportError: The error occured because of a function week_temp  I have created from an older version.
It was resolved with the help of deleting the duplicate file and the DynamicArray class was imported correctly.

ModuleNotFoundError: When running tests from inside the tests folder, the program could not find the package data_structures.
The issue was resolved by running pytest from the project root and adding a relative path adjustment to sys.path.

PowerShell command error: Deleting cache folders required the correct PowerShell syntax:
Remove-Item -Recurse -Force __pycache__.

Conclusion

It provides an easy-to-understand model for operations like access, insertion, and removal, while keeping performance optimal for most use cases.

The entire process of development is also demonstrated here:
testing - implementation - debugging - validation,
and is the foundation of the analysis of data structure design and analysis in Python.