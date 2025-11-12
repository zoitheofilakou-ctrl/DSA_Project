# --------------- Stack Implementation ---------------------

# Stack for browser history (LIFO)

# ----------------------------------------------------------
class Stack:
    # create a list
    def __init__(self):
        self.items = [] #empty

    # add items - page  (top)
    def push(self, item):
        self.items.append(item)
        print(f"Visited: {item}")

    #delete and return the one added
    def pop(self):
        if self.is_empty():
            print("No option to go back")
            return  None
        
        removed = self.items.pop() #delete the top element
        print(f"\nBack to previous page {removed}")
        return removed
    
    def peek(self):
        #return last item without removing 
        if self.is_empty():
            print("There is no page to open")
            return None
        
        return self.items[-1] #get top element
    
    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("\nBrowser History (top --> bottom)")
        for page in reversed(self.items): #top item first
            print(page)

# --------------------- Stack Demo -------------------------------

def stack_demo():
    brows_hist = Stack()

    #add pages
    brows_hist.push("github.com")
    brows_hist.push("spotify.com")
    brows_hist.push("google.com")
    brows_hist.push("kivuton.fi")

    #show stack
    brows_hist.display()

    # press back
    brows_hist.pop()
    
    #find current
    print("\nCurrent page", brows_hist.peek())

    #show again 
    print("\nAfter returning")
    brows_hist.display()




# --------------- Queue Implementation ---------------------

# Call Center -Customer Support  (FIFO)

# ----------------------------------------------------------


from collections import deque

# FIFO of a queue for a customer service 
# deque more efficient for removal from the beginning
class CallCenterQueue: 
    def __init__(self):
        self.queue = deque() # Deque = Double-ended queue(add-remove both ends)

    # add costumer at the end
    def add_customer(self, name):
        self.queue.append(name)
        print(f"Customer '{name}' is added to the queue.")
    
    # Serving  the first costumer
    def current_customer(self):
        if self.is_empty():
            print("No costumers to serve")
            return None
        served = self.queue.popleft() #remove 1st item from the list and return it
        print(f"Customer '{served}' has been served.")
        return served
    
    # show next costumer without removing
    def next_customer(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Next customer: {self.queue[0]}")
        return self.queue[0] #the first element of the list
    
    #show all costumers in the queue
    def display_queue(self):
        if self.is_empty():
            print("Empty queue")
        else:
            print("\nCurrent queue:", "-->" .join(self.queue))

    #check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    



