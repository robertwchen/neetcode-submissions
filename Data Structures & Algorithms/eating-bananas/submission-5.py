import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)

        # rate 0 -> 1 -> max_rate
        left = 1
        right = max_rate

        while left < right:
            mid = (left + right) // 2 # a rate
            # how long does this rate take?
            current_h = 0 # how long midpoint takes
            for pile in piles:
                current_h += math.ceil(pile / mid)
            
            if current_h > h:         # satsifies!
                # search right
                left = mid + 1

            elif current_h <= h:
                right = mid
            
        return left
            



        