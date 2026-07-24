# where am I
# what am I doing
# what do I return

# [2,   -3,    4,    -2]. [-1]
#                         p1.  p2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        current_sum = 0
        max_sum = float('-inf')

        for right in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
                left = right
            
            current_sum += nums[right]
            max_sum = max(current_sum, max_sum)
        return max_sum
