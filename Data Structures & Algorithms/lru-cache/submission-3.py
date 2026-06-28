class Node:
    def __init__(self, key = 0, val = 0):
        self.next, self.prev = None, None
        self.key, self.val = key, val
        
class LRUCache:

    def __init__(self, capacity: int):
        self.main = {}
        self.left, self.right = Node(), Node()
        self.right.prev = self.left
        self.left.next = self.right
        

        self.cap = capacity
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        node.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.main:
            self.remove(self.main[key])
            self.insert(self.main[key])
            return self.main[key].val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.main:
            self.remove(self.main[key])
        self.main[key] = Node(key, value)
        self.insert(self.main[key])
        if len(self.main) > self.cap:
            rem = self.left.next.key
            node = self.main[rem]
            self.remove(node)
        
            del self.main[rem]
        

        
