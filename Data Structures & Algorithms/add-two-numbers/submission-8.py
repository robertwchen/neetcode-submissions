# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# in reverse order 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add 2 numbers and trigger carry
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2:
            # calculate sum

            # calculate the carry bit
            left_val = l1.val if l1 else 0
            right_val = l2.val if l2 else 0
            total_sum = (left_val + right_val + carry) # compute current val
            digit = total_sum % 10
            carry = (total_sum) // 10 # compute next carry

            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            tail.next = ListNode(1)

        return dummy.next

        current = dummy.next
        while current is not None:
            print(current.val)
            current = current.next
        


            
            
