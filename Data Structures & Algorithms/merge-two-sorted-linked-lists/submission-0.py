# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # so basically zipper the two
        # start with new tail = dummy node
        dummy = ListNode()
        tail = dummy

        tail1 = list1
        tail2 = list2

        while tail1 is not None and tail2 is not None:
            if tail1.val < tail2.val:
                tail.next = tail1
                tail1 = tail1.next
                tail = tail.next
            
            else:
                tail.next = tail2
                tail2 = tail2.next
                tail = tail.next

        if tail1 is None:
            tail.next = tail2
        if tail2 is None:
            tail.next = tail1
        return dummy.next

        # now if one of them are none
            # add tail of other
        # if 2nd one is none
            # add tail of first

        