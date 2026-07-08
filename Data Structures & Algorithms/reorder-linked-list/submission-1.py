# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle node
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse second half
        dummy = None 
        prev = dummy
        current = second
        
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        reversed_head = prev
        # use head
        
        current = head
        p1 = head
        p2 = reversed_head

        while p2 is not None:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
        return

        
        