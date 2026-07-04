class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for i in range(0, len(nums)):
            if (nums[i] not in count_map):
                count_map[nums[i]] = 0
            count_map[nums[i]] += 1
        
        for i in range(0, len(nums)):
            if count_map[nums[i]] > 1:
                return True
        return False





        
        
        