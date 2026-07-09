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
        
        result = ListNode(0)
        current = result
        p1 = l1
        p2 = l2
        carry = 0
        while p1 is not None and p2 is not None:
            sum = (p1.val + p2.val + carry) % 10
            print(f"sum: {sum}")
            carry = (p1.val + p2.val + carry) // 10
            print(f"carry: {carry}")
            current.val = sum
            print(f"current.val: {current.val}")
            if p1.next is not None or p2.next is not None:
                current.next = ListNode(0)
                current = current.next
            p1 = p1.next
            p2 = p2.next

        while p1 is not None:
            sum = (p1.val + carry) % 10
            print(f"sum: {sum}")
            carry = (p1.val + carry) // 10
            print(f"carry: {carry}")
            current.val = sum
            
            if p1.next is not None:
                current.next = ListNode(0)
                current = current.next
            p1 = p1.next

        while p2 is not None:
            sum = (p2.val + carry) % 10
            carry = (p2.val + carry) // 10
            current.val = sum
            
            if p2.next is not None:
                current.next = ListNode(0)
                current = current.next
            p2 = p2.next
            
            
        if carry != 0:
            current.next = ListNode(carry)

        return result




            
            
        