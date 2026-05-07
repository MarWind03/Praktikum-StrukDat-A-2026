class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
    
    def print_forward(self):
        current = self.head
        while current:
            print(f"{current.judul} by {current.pengarang}", end = " <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next

        while current:
            print(f"{current.judul} by {current.pengarang}", end = " <-> ")
            current = current.prev
        print("None")

    def delete_by_judul(self, judul):
        current = self.head

        while current:
            if current.judul == judul:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return
            current = current.next
dll = DoublyLinkedList()
dll.insert_tail("Laskar Pelangi", "orang")
dll.insert_tail("Bumi Manusia", "orang2")
dll.insert_tail("Sang Pemimpi", "orang3")
print("Dari depan ke belakang : ")
dll.print_forward()

print("Dari belakang ke depan : ")
dll.print_backward()

print("Menghapus Bumi Manusia")
dll.delete_by_judul("Bumi Manusia")
dll.print_forward()
