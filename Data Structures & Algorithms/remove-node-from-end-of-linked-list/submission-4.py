# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # start from 0 mark nth node

        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        
        steps = length - n
        print(steps)


        dummy = ListNode()
        dummy.next = head
        current = dummy
        for i in range(steps):
            current = current.next
        current.next = current.next.next
        return dummy.next



        