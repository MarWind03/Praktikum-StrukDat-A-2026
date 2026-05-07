class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def tampilkan_antrean(head):
    curNode = head
    while curNode.next:
        print(f"{curNode.data}", end=" -> ")
        curNode = curNode.next
    print(f"{curNode.data} -> Null")

def sisipkan_vip(head, plat_baru, plat_target):
    curNode = head
    while curNode.next and curNode.next != plat_target:
        curNode = curNode.next
    
    if curNode.next == None:
        return head
    
    plat_baru.next = curNode.next.next
    curNode.next.next = plat_baru
    return head

Node1 = Node("BM 259 AB")
Node2 = Node("BM 259 AC")
Node3 = Node("BM 259 AD")

Node1.next = Node2
Node2.next = Node3

tampilkan_antrean(Node1)

Node4 = Node("B 237 AM")
Node1 = sisipkan_vip(Node1, Node4 , Node2)
tampilkan_antrean(Node1)