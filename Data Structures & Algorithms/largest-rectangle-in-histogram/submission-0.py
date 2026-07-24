



# monotonic stack to calculate next lowest height and index
# both ways
# [7, 1, 7, 2, 2, 4]
# [0, 1, 0, 2, 1, 0]
# 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_lens = self.calculate_tail(heights)
        reversed_heights = heights[::-1]
        right_lens = (self.calculate_tail(reversed_heights))[::-1]
        max_area = 0
        for i, height in enumerate(heights):
            area = height * (1 + left_lens[i] + right_lens[i])
            max_area = max(area, max_area)
        return max_area

    def calculate_tail(self, heights):
        stack = []
        lengths = [0 for i in range(len(heights))]
        stack.append((heights[0], 0))

        for i in range(1, len(heights)):
            while stack and heights[i] < stack[-1][0]:
                prev_h, prev_i = stack.pop()
                lengths[prev_i] = i - prev_i - 1

            stack.append((heights[i], i))
        for h, i in stack:
            lengths[i] = len(heights) - i - 1
        return lengths
        



            