# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# where am I
# what am I doing
# what do I return
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0

        for node in lists:
            heapq.heappush(heap, (node.val, count, node))
            count += 1
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, count, current = heapq.heappop(heap)
            tail.next = current
            tail = tail.next

            nxt = current.next
            if current.next:
                heapq.heappush(heap, (nxt.val, count, nxt))
                count += 1
        
        return dummy.next