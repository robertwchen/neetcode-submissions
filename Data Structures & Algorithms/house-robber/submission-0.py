# where am I
    # at some house
# what am I doing
    # deciding whether to rob house or skip
# what do I return
    # max profit

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self._rob(nums, 0, {})
    

    def _rob(self, nums, i, memo):
        if i in memo:
            return memo[i]
        if i >= len(nums):
            return 0

        # I am at hosue rob or skip
        rob_house = nums[i] + self._rob(nums, i + 2, memo)
        skip_house = self._rob(nums, i + 1, memo)

        memo[i] = max(rob_house, skip_house)
        return memo[i]
        