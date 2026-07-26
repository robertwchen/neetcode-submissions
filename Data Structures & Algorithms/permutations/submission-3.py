# where am I
    # at some point on array
# what am I doing
# what do I return

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i):
            if i == len(nums):
                return [[]]

            current = nums[i]
            all_perms = []

            for perm in dfs(i + 1):
                for i in range(len(perm) + 1):
                    all_perms.append(perm[:i] + [current] + perm[i:])
            return all_perms

        return dfs(0)
            
