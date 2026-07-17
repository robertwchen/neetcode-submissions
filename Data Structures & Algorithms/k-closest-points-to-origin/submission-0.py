# where am I
    # I am processing a point in points pushing it to minstack
# what am I doing
    # I decide what value to sort by in minstack
# what do I return
    # return the closest point

import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max stack shape: [ (-distance, [point])]
        x1 = 0
        y1 = 0
        max_stack = []
        for point in points:
            x2, y2 = point[0], point[1]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            heapq.heappush(max_stack, (-distance, point))
            if len(max_stack) > k:
                heapq.heappop(max_stack)
        
        result = []
        for distance, point in max_stack:
            result.append(point)
        return result

        # first push points into the stack
        # for each element push in
            # if len(max_stack) > k:
                # pop largest element

        #loop through max_stack create the array of points
        
        