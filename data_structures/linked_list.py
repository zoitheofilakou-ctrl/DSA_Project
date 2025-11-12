# Linked List - songs

# Create a class for nodes (data + pointer)
class Node:
    def __init__(self, data):
        self.data = data  # node value
        self.next = None  # pointer to next node


class LinkedList:
    def __init__(self):
        self.head = None  # empty list

    # Add song at the end
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node  # first node becomes head
        else:
            current = self.head  # temporary pointer
            while current.next:
                current = current.next
            current.next = new_node

    # Remove first song
    def remove_first(self):
        if self.head:
            self.head = self.head.next  # move head to next node

    # Display the playlist
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
