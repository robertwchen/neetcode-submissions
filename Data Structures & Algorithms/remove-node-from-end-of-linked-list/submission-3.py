# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1 2 3 4 5] 2
#.    back  front
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        for i in range(n):
            front = front.next
        
        dummy = ListNode()
        dummy.next = head
        back = dummy
        while front:
            front = front.next
            back = back.next

        back.next = back.next.next
        return dummy.next