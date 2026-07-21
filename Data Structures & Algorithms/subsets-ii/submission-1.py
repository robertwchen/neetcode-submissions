# where am I
    # at some number deciding to include or exclude
# what am I doing
    # including or excludng
# what do I return
    # all subsets but no duplicates

# [1, 1, 2]       
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        nums.sort()
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # include
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            #exclude always skip to next real char
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return result

            
            