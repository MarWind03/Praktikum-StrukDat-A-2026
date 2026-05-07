# BAGIAN 1
class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)
        
    def pop(self):
        if self.is_empty():
            print("Riwayat masih kosong")
        else:
            return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
stack = StackList()
print(stack.is_empty())
stack.push('w3s')
print(stack.peek())
stack.push('gcr')
print(stack.is_empty())
print(stack.size())
stack.push('satuunri')
print(stack.peek())
stack.pop()
print(stack.peek())
print()

# BAGIAN 2
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        return self.top is None

    def push(self, url):
        newNode = Node(url)
        newNode.next = self.top
        self.top = newNode
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Riwayat Masih Kosong")
        else:
            val = self.top.url
            self.top = self.top.next
            self.count -= 1
            return val
     
    def peek(self):
        return self.top.url
    
    def size(self):
        return self.count
    
stack = StackLinkedList()
print(stack.is_empty())
stack.push('w3s')
print(stack.peek())
stack.push('gcr')
print(stack.is_empty())
print(stack.size())
stack.push('satuunri')
print(stack.peek())
stack.pop()
print(stack.peek())
print()