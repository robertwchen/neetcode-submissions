
# [2, -3, 4]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        left = 0
        right = 0
        cur_sum = 0

        for right in range(len(nums)):
            # calculate max up to this point
            num = nums[right]
            if cur_sum < 0:
                left = right
                cur_sum = 0
            
            # then consider current num
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
        return max_sum
