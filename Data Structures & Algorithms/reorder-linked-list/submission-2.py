# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# [0, 1, 2, 3] [4, 5, 6]
# [0, 1, 2, 3] [6, 5, 4]
# zipper merge then attach remainder
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        mid_prev = self.findMiddle(head)
        mid = mid_prev.next
        mid_prev.next = None

        head2 = self.reverseList(mid)
        
        head = self.merge_list(head, head2)
        return

    def findMiddle(self, head):
        slow = head
        fast = head
        fast = fast.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        #dummy = ListNode(0)
        #dummy.next = head
        
        prev = None
        current = head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt


        return prev
    
    def merge_list(self, head1, head2):
        dummy = ListNode(0)
        
        p1 = head1
        p2 = head2

        tail = dummy
        while p1 and p2:
            tail.next = p1
            p1 = p1.next
            tail = tail.next
            tail.next = p2
            p2 = p2.next
            tail = tail.next
        if p1:
            tail.next = p1
        elif p2:
            tail.next = p2
        return dummy.next
        
