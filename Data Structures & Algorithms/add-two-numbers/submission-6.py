# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Slow: what is the brute force?
            # iterate through both and store as int, then add 
        #Repeat: what repeated work makes brute force slow?
            # conversion from ds to another 
        #Store: what do I keep so I do not repeat work?
            # I store the carry bit, along with p1 and p2 denoting current element to process
        #Move: exactly when do pointers move / stack pop / heap push-pop?
            # pointer moves up once at each digit, carry bit 
        #Answer: when do I update result?
            # at each iteration I append to the string or list
        #Test: quick edge case + time/space.
            # when you get to the end current is none 
            # different length -> add the tail of the other one
        
        dummy = ListNode(0)
        current = dummy
        carry = 0

        p1 = l1
        p2 = l2

        while p1 is not None or p2 is not None or carry:
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0

            total = (val1 + val2 + carry)
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        return dummy.next






            
            
        