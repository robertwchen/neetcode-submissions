# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [2  4 ]
# [8 6]
# [1. 3. 5]
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        nxt = slow.next
        slow.next = None

        dummy = None
        prev = dummy
        current = nxt
        while current is not None:
            after = current.next
            current.next = prev
            prev = current
            current = after
        # prev is the front


        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            
            first, second = tmp1, tmp2



