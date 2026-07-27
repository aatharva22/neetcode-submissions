class DLL:
    def __init__(self,key = 0, val = 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.head = DLL()
        self.tail = DLL()
        self.head.prev = None
        self.tail.next = None
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _delete(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _insert(self,node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        


    def get(self, key: int) -> int:

        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self._delete(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.hmap:
            self._delete(self.hmap[key])
        node = DLL(key,value)
        self.hmap[key] = node
        self._insert(node)

        if len(self.hmap) > self.capacity:

            lru = self.tail.prev
            self._delete(lru)
            del self.hmap[lru.key]
        
        

