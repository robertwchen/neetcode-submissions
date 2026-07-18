# where am I
    # at some num on the array
# what am I doing
    # deciding whether to include or not
# what do i return
    # return array of all subsets with and without the element

# [2, 3] 
# [[]] -> [[3], []] -> [3, 2], [], [2], [2, 3]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        # form without
        first_num = nums[0]
        without_subsets = self.subsets(nums[1:])

        with_subsets = []
        for subset in without_subsets:
            with_subsets.append([first_num, *subset])

        return without_subsets + with_subsets

        # form with
        
        