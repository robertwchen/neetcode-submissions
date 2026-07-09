"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create copy hashmap
        copy_map = {}

        # loop through original linkedlist
            # create copy node with val of current
            # add to hashmap
            # then go to next
        if head is None:
            return None

            
        current = head
        while current is not None:
            copy = Node(current.val)
            copy_map[current] = copy
            current = current.next

        # second loop now need to wire it to the next one and the pointer 
            # take each one find the node.next
    
        current = head
        while current is not None:
            copy = copy_map[current]
            if current.next is None:
                copy.next = None
            else:
                copy.next = copy_map[current.next]

            if current.random is None:
                copy.random = None
            else:
                copy.random = copy_map[current.random]
            current = current.next
        return copy_map[head]

        
        