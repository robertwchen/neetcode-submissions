class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        # head node1 node2 tail
    def _remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        
    def _add(self, node):
        # wire node at the end
        prev_last = self.tail.prev
        prev_last.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev_last

    def get(self, key: int) -> int:
        if key in self.lookup:
            self._remove(self.lookup[key])
            self._add(self.lookup[key])
            return self.lookup[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            # don't change key
            node = self.lookup[key]
            self._remove(node)
            self._add(node)
            node.val = value

        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node

            if len(self.lookup) > self.capacity:
                first = self.head.next
                del self.lookup[first.key]
                self._remove(self.head.next) 
            
            self._add(new_node)

            
        
