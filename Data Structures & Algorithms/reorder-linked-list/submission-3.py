# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1 2 3 4 5]
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint , cut
        if head is None:
            return None

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        nxt = mid.next
        mid.next = None
        
        # reverse second half
        prev = None
        current = nxt

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        p2 = prev
        p1 = head
        # link up 2 at a time
# [2, 4]. # [8, 6]

        while p1 and p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2
            

