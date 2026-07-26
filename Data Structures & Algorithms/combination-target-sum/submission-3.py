# where am I
    # at some combination
# what am I doing
    # either try to add this eleemtn or move to the next one
# what do I return
    #
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        comb = []
        def dfs(i, amount):
            if amount == 0:
                result.append(comb.copy())
                return
            if amount < 0:
                return

            if i >= len(nums):
                return

            comb.append(nums[i])
            dfs(i, amount - nums[i])
            comb.pop()
            dfs(i + 1, amount)
        dfs(0, target)
        return result 
    
