# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# where am I
    # at some point on linked list
# what am I doing
    # loop throguh to find the length of the list
    # then loop through again
# what do I return

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        list_len = 0

        if head is None:
            return None

        while current is not None:
            list_len += 1
            current = current.next

        before_nth = list_len - n
        

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        for i in range(0, before_nth):
            current = current.next
        print(current.val)

        nth = current.next
        if nth is not None:
            nxt = nth.next
            current.next = nxt
        return dummy.next

        

