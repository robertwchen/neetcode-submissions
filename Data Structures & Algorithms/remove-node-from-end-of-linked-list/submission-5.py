# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # start from 0 mark nth node

        dummy = ListNode
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next
        print(fast.val)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next



        