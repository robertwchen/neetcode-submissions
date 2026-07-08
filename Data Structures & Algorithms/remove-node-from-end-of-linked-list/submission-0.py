# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass loop through find length of list
        # calculate the distance from first node using N
    

        current = head
        length = 0
        while current is not None:
            current = current.next
            length += 1
        print(f"length: {length}")

        k = length - n
        prev = None
        skip = None
        nxt = None
        current = head

        if k == 0:
            head = head.next
            return head

        for i in range(0, k + 1):
            print(f"index: {i} current:{current.val}")
            if i == k - 1:
                prev = current
            elif i == k:
                nxt = current.next if not None else None
                skip = current

            current = current.next
        #print(f"prev: {prev.val}")
        #print(f"skip: {skip.val}")
        #print(f"nxt: {nxt.val}")

        prev.next = nxt
        skip.next = None
        return head

        
            


           # [ 1, 2, 3]
            # 0  1   2  3
            #.   2   1\
        
            #[5] 

        # if length 0 return NOne
        