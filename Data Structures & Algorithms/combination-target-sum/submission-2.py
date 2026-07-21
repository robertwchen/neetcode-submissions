class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []

        def dfs(i, current_sum):
            if i == len(nums):
                return 
            if current_sum > target:
                return
            if current_sum == target:
                result.append(comb.copy())
                return

            comb.append(nums[i])
            dfs(i, current_sum + nums[i])
            comb.pop()
            dfs(i + 1, current_sum)
        
        dfs(0, 0)
        return result
            # remove 1
            # try 2