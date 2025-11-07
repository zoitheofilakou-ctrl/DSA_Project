# -------------- AVL organize students based on ID ----------------------------

#define node

class StudentNode:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1

# -------------- Auxiliary  Functions ------------------------------------------

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_left(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 +max(get_height(z.left), get_height(z.right))
    y.height = 1+ max(get_height(y.left), get_height(y.right))

    return y

def rotate_right(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 +max(get_height(z.left), get_height(z.right))
    y.height = 1+ max(get_height(y.left), get_height(y.right))

    return y

# ---------------------- Insert student in the tree -----------------------------------
#--------------------------------------------------------------------------------------
def insert(root, student_id, name):
    if not root:
        return StudentNode(student_id, name)
    
    if student_id < root.student_id:
        root.left = insert(root.left, student_id, name)
    elif student_id > root.student_id:
        root.right = insert(root.right, student_id, name)
    else: 
        return root # avoid double ID
    
    #update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    #compute balance
    balance = get_balance(root)

    # inbalance corrections
    if balance > 1 and student_id < root.left.student_id:   # LL
        return rotate_right(root)
    if balance < -1 and student_id > root.right.student_id:  # RR
        return rotate_left(root)
    if balance > 1 and student_id > root.left.student_id:    # LR
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and student_id < root.right.student_id:  # RL
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


# ------------------------Student search ---------------------------------------------
# ------------------------------------------------------------------------------------
def search(root, student_id):
    if not root:
        return None
    if student_id == root.student_id:
        return root.name
    elif student_id < root.student_id:
        return search(root.left, student_id)
    else:
        return search(root.right, student_id)
    
# -------------------------Display sorted students -----------------------------------
# ------------------------------------------------------------------------------------
def inorder(root):
    if root:
        inorder(root.left)
        print(f"{root.student_id} - {root.name}")
        inorder(root.right)


# ----------------------------Example Usage -----------------------------------------

root = None

students = [
    (5, "Maria"),
    (3, "Nikos"),
    (8, "Eleni"),
    (2, "Anna"),
    (4, "Kostas"),
]

for sid, name in students:
    root = insert(root, sid, name)

print("List of students sorted by ID:")
inorder(root)

print("\nSearch student with ID 4:")
result = search(root, 4)
if result:
    print("Found:", result)
else:
    print("No student with this ID")