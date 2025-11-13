### Hash Table Analysis

**Data Structure:** Hash Table  
**Scenario:** Email Registry  
**Source File:** data_structures/hash_table.py  

---

### Description

A Hash Table is a data structure designed for extremely fast data access by associating each value with a calculated index rather than storing elements sequentially.  
It uses a mathematical function — the **hash function** — to map each key (such as an email) to a position in an internal table.  
This enables near-instant lookup, insertion, and verification of data.  

In this project, the Hash Table is implemented as an **Email Registry**, where each email address is converted into a numeric index and stored in a corresponding “bucket.”  
When two emails share the same index (a collision), both are stored in a small list inside that bucket, a technique known as **separate chaining**.  
This simple yet effective model allows efficient management of unique entries, such as user databases or membership systems.

---

### Implementation Summary

The implementation is contained in a single class, **EmailRegistry**, which provides all core operations:  

- `__init__(size)` – initializes the table with a fixed number of empty buckets.  
- `hash_function(email)` – converts an email string into an integer index using the sum of ASCII values modulo the table size.  
- `add_email(email)` – adds a new email if it does not already exist; duplicates are ignored.  
- `exists(email)` – checks if an email is already registered.  
- `display()` – prints all table buckets and their contents for visualization.  

Collisions are handled by appending new entries to a list within the same index.  
This design keeps the structure simple while demonstrating how hashing manages collisions efficiently.

---

### Testing and Validation

Testing was performed using the **pytest** framework in `tests/test_hash_table.py`.  
Each test focused on logical correctness rather than printed output.  
Scenarios included adding emails, detecting duplicates, validating collision handling, and checking hash index boundaries.  
All tests passed successfully, confirming that insertion, lookup, and display operations functioned as expected.

---

### Time and Space Complexity

- **Insertion / Lookup:** O(1) average case, O(n) worst case (if many collisions)  
- **Space Complexity:** O(n), proportional to the total number of stored emails  

Although the hash function used here is intentionally simple, it clearly illustrates the concept of hashing.  
In practical systems, more sophisticated functions are used to reduce collisions and maintain constant-time performance.

---

### Debugging Notes

Minor fixes were made during development to improve stability:  

- Added an `exists()` method for easier validation during testing.  
- Verified that hash indices always stay within range.  
- Confirmed that collision handling through lists worked correctly.  
- Ensured pytest ran smoothly from the project root without import issues.  

After these corrections, the structure performed consistently in both tests and live demonstrations.

---

### Conclusion

The Hash Table provides a fast and reliable way to store and retrieve unique data through key-based indexing.  
In this project, it was applied as an **Email Registry**, demonstrating efficient data organization, duplicate prevention, and collision handling.  
This module follows the same workflow as previous ones — implementation, testing, debugging, and validation — while introducing the concept of associative data storage, bridging simple linear structures with more advanced mapping systems used in modern software.
