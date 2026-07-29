# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the midpoint
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now the middle
        second = slow.next
        slow.next = None


        prev = None
        current = second
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        

        head1 = head
        head2 = prev

        tail = ListNode()


#.    [1 2 3 4]
#     [8 7 6 5]

        while head1 and head2:
            next1, next2 = head1.next, head2.next
            tail.next = head1
            head1 = next1
            tail = tail.next

            tail.next = head2
            head2 = next2
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        