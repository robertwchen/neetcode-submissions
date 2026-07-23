# where am I
# what am I doing
# what do I return


class Solution:
    def maxArea(self, heights: List[int]) -> int:


        p1 = 0
        p2 = len(heights) - 1

        max_area = 0
        while p1 < p2:
            height_1 = heights[p1]
            height_2 = heights[p2]
            min_height = min(height_1, height_2)
            area = (p2 - p1) * min_height
            max_area = max(area, max_area)
            if height_1 < height_2:
                p1 += 1
            else:
                p2 -= 1

        return max_area
        