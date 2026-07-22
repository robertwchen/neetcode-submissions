# where am I
# what am I doing
# what do I return

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_first(nums, 0, {}), self.rob_last(nums, 1, {}))
        
    def rob_first(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums) - 1:
            return 0
        take = nums[i] + self.rob_first(nums, i + 2, memo)
        skip = self.rob_first(nums, i + 1, memo)
        memo[i] = max(take, skip)
        return memo[i]

    def rob_last(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0
        take = nums[i] + self.rob_last(nums, i + 2, memo)
        skip = self.rob_last(nums, i + 1, memo)
        memo[i] = max(take, skip)
        return memo[i]
        