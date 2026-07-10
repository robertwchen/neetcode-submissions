# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        current = groupPrev


        while True:
            start = groupPrev.next
            kth = self.get_kth(groupPrev, k) # returns the last node of segment or none
            if kth is None:
                break
            
            groupNext = kth.next
            kth.next = None 

            current = groupPrev.next
            prev = None

            while current is not None:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            groupPrev.next = kth
            groupPrev = start
            start.next = groupNext

        return dummy.next


            # then reverse till k points
            # point groupNext to k.next
            #groupPrev = kth
                    
    def get_kth(self, current, k):
        while current is not None and k > 0:
            k -= 1
            current = current.next
        return current


        