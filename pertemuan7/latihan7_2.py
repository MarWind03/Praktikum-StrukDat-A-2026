class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def tambahKendaraan(head, plat):
    curNode = head
    while curNode.next:
        curNode = curNode.next
    curNode.next = plat
    return head

def hapusKendaraan(head, plat):
    if head == plat:
        return head.next

    curNode = head
    while curNode.next and curNode.next != plat:
        curNode = curNode.next

    if curNode.next == None:
        return head
    
    curNode.next = curNode.next.next
    return head


def tampilkan_antrean(head):
    curNode = head
    while curNode.next:
        print(f"{curNode.data}", end=" -> ")
        curNode = curNode.next
    print(f"{curNode.data} -> Null")


plat1 = Node("BM 2592 AD")
plat2 = Node("A 231 BM")
plat3 = Node("B 128 KM")
plat4 = Node("A 78 H")

plat1.next = plat2
plat2.next = plat3

tampilkan_antrean(plat1)
plat1 = tambahKendaraan(plat1, plat4)
tampilkan_antrean(plat1)
plat1 = hapusKendaraan(plat1, plat2)
tampilkan_antrean(plat1)

