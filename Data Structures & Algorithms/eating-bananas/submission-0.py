import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intuition: 
        # Find: minimum eating speed k that satisfies the h it takes
        # Maintain: 
        # Broken by:
        # Fix:
        # Update Answer:

        max_k = max(piles) #max bananas per hour

        # search from 1 to k:
        p1 = 1
        p2 = int(max_k)

        while p1 < p2:
            # calculate hours it takes to finish
            speed = (p1 + p2) // 2

            hours = 0
            for b in piles:
                hours += math.ceil(b / speed)
            if hours <= h:
                p2 = speed 
            if hours > h:
                p1 = speed + 1 

        return p1

            # speed to large try smaller (move right pointer down)
            # if speed to small move small pointer up
        # return left pointer which represents the minimum valid speed at the end 



        



