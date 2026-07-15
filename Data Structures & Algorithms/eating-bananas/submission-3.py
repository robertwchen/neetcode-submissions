import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
# Return:
# What exactly am I returning?
    # minumum k eating rate

# Example:
# Tiny input + expected output by hand
    # [1, 4, 3, 2] h = 9, 2 

# Brute:
# Dumb obvious way, even if slow
    # try every possible rate from 1 -> max_rate to find the minimum rate

# Property:
# What special clue can improve brute force?
# sorted? BST? contiguous? frequency? top k? level order?
    # piles

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
    # binary search
# State:
# What variables/data structures do I need?
    # p1 p2, calculate hours to finish bananas

# Invariant:
# What must stay true?
    # rate must be rounded up

# Progress:
# What moves/changes each step?
    # 


# Update:
# When do I count/save/return answer?
    # when target hours is found 
        # [ 3 4 5]

        max_rate = max(piles) # first find max possible rate 

        left = 1
        right = max_rate
        while left < right:# binary search for minimum target hours:
            
            mid = (left + right ) // 2 # mid = ???
            
            hours = 0
            for n in piles:
                # round down + 1
                hours += math.ceil(n / mid)
            print(mid, hours)
            # calculate how many hours given current rate
            
            if hours <= h: # if mid < hours.  decrease rate
                right = mid

            if hours > h:# if mid > hourse.  increase rate
                left = mid + 1
            
        return right
        