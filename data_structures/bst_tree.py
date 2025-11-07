# ---------------------------------BSTree - Sales-------------------------------------

class Node: 
    def __init__(self, value):
        self.value = value  # each node has a value
        self.left = None
        self.right = None


class SalesBSTree:  
    def __init__(self):
        self.root = None   

    def insert(self, value):  # add new value
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)  

    def insert_recursive(self, current, value):  # recursive insertion of a price
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)

    def inorder_display(self, node):
        # display in ascending order
        if node:
            self.inorder_display(node.left)
            print(node.value, end=" ")
            self.inorder_display(node.right)


# -----------------------------------------Demo----------------------------------------

def bst_demo():
    bst = SalesBSTree() 

    # add prices 
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    print("Sorted Sales:")
    bst.inorder_display(bst.root)
    print()


if __name__ == "__main__":
    bst_demo()
