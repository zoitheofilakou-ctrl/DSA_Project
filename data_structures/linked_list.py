### Linked List - songs

# Create a class for nodes(data - pointers)

class Node():
    def __init__(self, data):
        self.data = data #node value
        self.next = None #pointer 

class LinkedList():
    def __init__(self):
        self.head = None #empty list

    # add song at the end
    def add(self, data): 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node #1st song becomes head
        else:
            current = self.head #temporary pointer 
            while current.next: 
                current = current.next
            current.next = new_node 

    def remove_first(self):
        if self.head:
            self.head = self.head.next #move head to next


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# Demo for LinkedList functionality
# Only runs when the file is run directly.
# Creates a LinkedList object and tests
# the basic functions: add, delete, display.
# --------------------------------------------------------

if __name__ == "__main__":

    #create new linked list
    playlist = LinkedList()


    #add some songs
    playlist.add ("Imagine")
    playlist.add ("Black Sabbath")
    playlist.add ("Hotel California")

    #show playlist
    playlist.display()

    # Delete first  song
    playlist.remove_first()
    print("After deletion:", playlist.display()) 

    #Add new song
    playlist.add("Let it be")
    print("After addition:", playlist.display())
