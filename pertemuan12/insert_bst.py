class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        P = Q = self.root
        while Q is not None and P.data != new_node.data:
            P = Q
            if new_node.data < P.data:
                Q = P.left
            else:
                Q = P.right
            
        if P.data == new_node.data:
            print("Data Duplikat!")
            return

        if P.data > new_node.data:
            P.left = new_node
        else:
            P.right = new_node       
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent, data):
        new_node = Node(data)
        if parent.left is None:
            parent.left = new_node
            return
        new_node.left = parent.left
        parent.left = new_node

    def insert_right(self, parent, data):
        new_node = Node(data)
        if parent.right is None:
            parent.right = new_node
            return
        new_node.right = parent.right
        parent.right = new_node

def preorder(node):
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


bst = BinarySearchTree()

bst.insert(45)
bst.insert(9)
bst.insert(5)
bst.insert(8)
bst.insert(7)

inorder(bst.root)
print()

bt = BinaryTree()
bt.insert_root('F')
bt.insert_left(bt.root, 'B')
bt.insert_right(bt.root, 'G')
bt.insert_left(bt.root.left, 'A')
bt.insert_right(bt.root.left, 'D')
bt.insert_left(bt.root.left.right, 'C')
bt.insert_right(bt.root.left.right, 'E')
bt.insert_right(bt.root.right, 'I')
bt.insert_left(bt.root.right.right, 'H')

print("Preorder : ", end='')
preorder(bt.root)
print()
print("Inorder : ", end='')
inorder(bt.root)
print()
print("Postorder : ", end='')
postorder(bt.root)
