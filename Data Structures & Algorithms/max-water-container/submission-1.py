class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer
        max_area = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            val1 = heights[p1]
            val2 = heights[p2]
            current_area = min(val1, val2) * (p2 - p1)
            
            max_area = max(current_area, max_area)
            if val1 == val2:
                p1 += 1
                p2 -= 1
            else:
                if val1 < val2:
                    p1 += 1
                else:
                    p2 -= 1
                
        return max_area

            
            
            
        