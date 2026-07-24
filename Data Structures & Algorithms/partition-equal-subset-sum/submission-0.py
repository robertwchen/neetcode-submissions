# goal: find 1 subset that == sum of all nums/2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != target // 1:
            return False
 
        def dfs(i, target, memo):
            key = (i, target)
            if key in memo:
                return memo[key]

            if i >= len(nums):
                return False

            if target == 0:
                return True

            # take current
            take = dfs(i + 1, target - nums[i], memo)
            skip = dfs(i + 1, target, memo)
            memo[key] = take or skip
            return memo[key]

            # skip current
        return dfs(0, target, {})
        
        