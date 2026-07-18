# where am I
# what am I doing
# what do I return 

# [3, 9] -> 
# if target < 0 return 0
# if target == 0 return [[]]


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def _combinationSum(start_index, target):
            if target < 0:
                return []
            if target == 0:
                return [[]]
            
            all_combinations = [] # stores all
            for i in range(start_index, len(nums)):
                num = nums[i]
                for comb in _combinationSum(i ,target - num): #returns me [[3]]
                    all_combinations.append([num, *comb])
            return all_combinations
        
        return _combinationSum(0, target)
