class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
        print("[INFO] Membangun Struktur Gudang...")
        print("[INFO] Struktur berhasil dibuat.")

    def traverse_preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end=' ')
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=' ')

    def get_leaf_nodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self.get_leaf_nodes(node.left)
            self.get_leaf_nodes(node.right)


print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print('=' * 38)
print()

BT = BinaryTree()
BT.insert_manual()
print()

print("HASIL AUDIT:")
print("1. Pre-Order  : ", end='')
BT.traverse_preorder(BT.root)
print("\n2. In-Order   : ", end="")
BT.traverse_inorder(BT.root)
print("\n3. Post-Order : ", end="")
BT.traverse_postorder(BT.root)
print('\n')

print("[DATA] Gudang Ujung (Leaf Nodes): ", end='')
BT.get_leaf_nodes(BT.root)
print()
print('=' * 38)
print("Audit Selesai!")
