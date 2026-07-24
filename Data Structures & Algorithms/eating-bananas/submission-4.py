# where am I
# what am I doing
# what do I return

# [1, 4, 3, 2] h = 9

# speed = 1, 2 -> 2 per hour 10 hours
# speed = 2,   6 hours -> under 10

# 1 < k < ?

# min < k < ?
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles) # returns -> 4
        lo = 1
        hi = max_k
        # 1 <= k <= max_k 
        # [1..2.. 4] mid = 2 -> takes
        # [1] current = 6 
        while lo < hi:
            mid = (lo + hi) // 2

            current_h = 0
            for pile in piles:
                current_h += math.ceil(pile / mid)
                # h = 6
            if current_h > h:
                lo = mid + 1
            elif current_h <= h:
                hi = mid
        return lo
