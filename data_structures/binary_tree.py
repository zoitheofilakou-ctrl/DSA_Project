# ---------------Binary Tree --------------------------

# Sales Analysis with Binary Tree

# -----------------------------------------------------

class Node: #tree node - includes a decision
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class SalesAnalysisTree:

    #decision making with binary on sales data
    def __init__(self):
        self.root = Node("Region = North?") #root

        #next nodes
        self.root.left = Node ("Season = Winter?") # Yes-->North
        self.root.right = Node("Sales : Low") #No

        #level 2
        self.root.left.left = Node ("Sales: High") # Yes , North + Winter
        self.root.left.right = Node( "Sales: Moderate") # Yes , North + Not Winter

     #recursive display of the tree
    def display(self, node, level=0):
        if node:
            print(' ' * level +f'{node.data}') # print current node
            self.display(node.left, level + 1)
            self.display(node.right, level +1)

def tree_demo():
    print("Decision tree for sales analysis")
    sales_tree = SalesAnalysisTree()
    sales_tree.display(sales_tree.root)

if __name__ == '__main__':
    tree_demo()



