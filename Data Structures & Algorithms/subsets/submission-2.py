# where am I
    # at some point on the nums array
# what am I doing
    # either take num or skip it
# what do I return
    # array of all nums

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # try
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            dfs(i + 1)
        dfs(0)
        return  result