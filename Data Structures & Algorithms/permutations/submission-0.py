# where am I
    #at some number in call stack
# what am I doing
    # placing the number at every possible position
# what do I return
    # all permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def _permute(nums, i):
            if i == len(nums):
                return [[]]
        
            first_num = nums[i]
            all_perms = []
            for perm in _permute(nums, i + 1):
                for j in range(len(perm) + 1):
                    all_perms.append(perm[:j] + [first_num] + perm[j:])
            return all_perms
        return _permute(nums, 0)