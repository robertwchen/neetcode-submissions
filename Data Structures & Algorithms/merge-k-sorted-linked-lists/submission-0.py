# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case different length 
        # queue up 1 2 3 
        # the queue up 2, 3, 1
        
        # start with dummy
        # size k min heap
        k = len(lists)
        heap = []
        dummy = ListNode(0)
        current = dummy

        if not lists:
            return None
        

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
           # pop smallest node
           val, i, new = heapq.heappop(heap)
           # attach it to result
           current.next = new
           current = current.next
           if new.next is not None:
                heapq.heappush(heap, (new.next.val, i, new.next))
            
        return dummy.next
                

            # pop smallest node 
        