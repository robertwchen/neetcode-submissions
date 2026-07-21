# where am I
    # at some point on the array
# what am I doing
    # try without then try with
# what do I return
    # all subsets
class Solution:
    # [3] -> [[]] , [[3]] combine -> [[], [[3]]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                results.append(subset.copy())
                return

            subset.append(nums[i])
            print(subset)
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)

        return results
        

        
        