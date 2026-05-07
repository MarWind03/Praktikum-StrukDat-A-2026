class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.urut = 1

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        P = Q = self.root
        while Q is not None and P.id_buku != new_node.id_buku:
            P = Q
            if new_node.id_buku < P.id_buku:
                Q = P.left
            else:
                Q = P.right
            
        if P.id_buku > new_node.id_buku:
            P.left = new_node
        else:
            P.right = new_node     
        
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku):
        print(f"[SEARCH] Mencari ID {id_buku}...", end=" ")

        cur_node = self.root
        ketemu = False
        while cur_node is not None:
            if cur_node.id_buku > id_buku:
                cur_node = cur_node.left
            elif cur_node.id_buku < id_buku:
                cur_node = cur_node.right
            else:
                ketemu = cur_node.judul
                break
        if ketemu:
            print(f"Ditemukan! Judul: {ketemu}")
        else:
            print("Data tidak ditemukan.")

    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"{self.urut}. {node.id_buku} - {node.judul}")
            self.urut+=1
            self.traversal_inorder(node.right)

    def get_min(self):
        cur_node = self.root
        if cur_node is None:
            return

        while cur_node.left is not None:
            cur_node = cur_node.left
        
        print(f"[STATISTIK] ID Terkecil: {cur_node.id_buku}")
        
    def get_max(self):
        cur_node = self.root
        if cur_node is None:
            return

        while cur_node.right is not None:
            cur_node = cur_node.right
        
        print(f"[STATISTIK] ID Terbesar: {cur_node.id_buku}")

    def height(self, node):

        if node is None:
            return 0
    
        return 1 + max(self.height(node.left), self.height(node.right))
    
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print('=' * 40)

BST = BinarySearchTree()
BST.insert('50', 'Dasar Pemrograman')
BST.insert('30', 'Struktur Data')
BST.insert('70', 'Kecerdasan Buatan')
BST.insert('20', 'Matematika Diskrit')
BST.insert('40', 'Basis Data')
BST.insert('60', 'Jaringan Komputer')
BST.insert('80', 'Sistem Operasi')
print()

print("[INFO] Koleksi Buku (In-Order Traversal):")
BST.traversal_inorder(BST.root)
print()

BST.search('60')
BST.search('100')
print()
        
BST.get_min()
BST.get_max()
print(f"[INFO] Tinggi (Height) Tree: {BST.height(BST.root)}")
print('=' * 40)
print('Simulasi Selesai!')

    


    