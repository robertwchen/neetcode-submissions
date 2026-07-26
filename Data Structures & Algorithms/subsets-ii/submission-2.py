class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                return

            current = nums[i]
            subset.append(current)
            result.append(subset.copy())
            dfs(i + 1)
            subset.pop()

            while i < len(nums) and nums[i] == current:
                i += 1
            
            dfs(i)
        dfs(0)
        return result
            