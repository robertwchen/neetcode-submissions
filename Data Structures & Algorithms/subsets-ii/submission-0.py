# where am I
    # at some number on array
# what am I doing
    # skip or add num
# what do I return
     # all subsets and sets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def _subsetsWithDup(nums, i):
            if i == len(nums):
                return [[]]
            
            # exclude element
            first_num = nums[i]
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            exclude_subset = _subsetsWithDup(nums, next_i) # returns subset

            all_include = []
            include_subset = _subsetsWithDup(nums, i + 1) # returns subsets of every element
            for subset in include_subset:
                all_include.append([first_num , *subset])
            return exclude_subset + all_include
        return _subsetsWithDup(nums, 0)
            # include element