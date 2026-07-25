# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# where am I
# what am I doing
# what do I return
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        current = head
        print(current.val)
 
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
        