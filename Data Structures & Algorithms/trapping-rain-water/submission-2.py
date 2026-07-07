class Solution:
    def trap(self, height: List[int]) -> int:
        # intuition we know at every point water stored is the min(max_left, max_right)
        # but instead of building the array, we can observe which ones can we check? well
        # we can check left side as long as left max is les than right max
        max_left = height[0]
        max_right = height[len(height) - 1]

        result = 0
        p1 = 1
        p2 = len(height) - 2 

        while p1 <= p2:
            # pick the minimum between max_left and max_right
            if max_left <= max_right:
                current_height = height[p1]
                water_store = max_left - current_height
                result += max(0, water_store)
                max_left = max(current_height, max_left)
                p1 += 1
            else:
                current_height = height[p2]
                water_store = max_right - current_height
                result += max(0, water_store)
                max_right = max(current_height, max_right)
                p2 -= 1
        return result
                # store current_solution


            