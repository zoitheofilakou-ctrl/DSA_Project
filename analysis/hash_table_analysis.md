# Hash Table Analysis

Data Structure: Hash Table  
Scenario: Email Registry System  
Source File: data_structures/hash_table.py

---

## Description

A hash table stores data in buckets using a hash function.
Each new value (email address) is converted into an index
based on the sum of its character codes (mod table size).

If two emails produce the same index, they are stored in the same bucket (list).
This is called a **collision**, and it is handled using **chaining**.

In this example:
- The registry can quickly add and check email addresses.
- Duplicates are prevented.
- Collisions are managed safely.

---

## Time and Space Complexity

- Add email → O(1) average time
- Search email → O(1)
- In worst case (many collisions) → O(n)
- Space → O(n), where n is the number of stored emails

---

## Notes

- On average, hash tables are extremely fast (O(1)).
- Collisions can make operations slower (up to O(n)).
- The efficiency depends on the **hash function** and the **table size**.
- Space grows linearly with the number of stored elements (O(n)).

---

## Performance Observation

Adding or searching a few emails was instant.
When the table size is small, some emails share the same bucket (collision),
but operations still finish very fast.

This matches the expected O(1) behavior for most cases.
