class Solution:
    def trap(self, height: List[int]) -> int:
        # so at every point look at left and right
        max_left = []
        max_right = []

        max_height_left = 0
        for current_height in height:
            max_left.append(max_height_left)
            max_height_left = max(current_height, max_height_left)

        max_height_right = 0
        for i in range(len(height) - 1, -1, -1):
            current_height = height[i]
            max_right.append(max_height_right)
            max_height_right = max(current_height, max_height_right)

        max_right.reverse()

        water_contained = 0
        for i, current_height in enumerate(height):
            min_height = min(max_left[i], max_right[i])
            water_stored = max(0, min_height - current_height)
            water_contained += water_stored  
        return water_contained



            