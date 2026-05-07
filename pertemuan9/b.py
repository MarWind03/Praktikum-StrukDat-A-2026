class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head
    
    def print_antrian(self):
        if self.head is None:
            print("Linked list kosong")
            return
    
        current = self.head

        while True:
            print(current.nama, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(kembali ke head)")

    def delete_head(self):
        if self.head is None:
            return
        current = self.head

        if current == self.head and current.next == self.head:
            self.head = None
        elif current == self.head:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head

cll = CircularLinkedList()
cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

cll.print_antrian()
cll.insert_tail("Edo")
cll.print_antrian()

cll.delete_head()
cll.print_antrian()
