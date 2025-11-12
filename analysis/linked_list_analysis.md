# Linked List Analysis

Data Structure: Linked List  
Scenario: Music Playlist  
Source File: data_structures/linked_list.py

---

## Description

This data structure connects elements one by one using "nodes".
Each node has some data (for example, a song title) and a pointer to the next node.
The Linked List is good for adding or removing items, because we can move from one node to another easily.

In my example, I used a music playlist:
- Add songs to the list
- Remove the first song
- Display the songs one by one

---

## Time and Space Complexity

- **Add a new node** at the end → O(n) time, because we must move through all nodes to find the last one.  
  Space → O(1), because only one node is created.

- **Remove the first node** → O(1) time, because we only change the head pointer.  
  Space → O(1)

- **Display all nodes** → O(n) time, because every node is printed once.  
  Space → O(1)

- **Access a node** (not implemented in my example) → O(n),  
  because in a linked list we must move through nodes one by one to reach a specific position.


---

## Notes

- Adding or removing at the start is fast (O(1)).
- Adding at the end is slower (O(n)), because we must reach the last node.
- Linked Lists use more memory than simple arrays, since each node needs an extra pointer (O(n) space overall).

---

## Conclusion

Linked Lists are flexible for adding or removing elements but slower for direct access.
They are useful when you don’t know the total number of items in advance or need to change the list often.
