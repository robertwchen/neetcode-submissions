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

        # reverse second half
        dummy = None 
        prev = dummy
        current = slow
        
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

        while current is not None:
            print(current.val)
            if current is p1:
                p1 = p1.next 
                current.next = p2

            elif current is p2:
                p2 = p2.next
                current.next = p1

            current = current.next
        return

        
        