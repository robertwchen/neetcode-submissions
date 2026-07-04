class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = self.counter(nums)
        
        for i in range(0, len(nums)):
            if count_map[nums[i]] > 1:
                return True
        return False

    def counter(self, num_array):
        count_array = {}
        for i in range(0, len(num_array)):
            if (num_array[i] not in count_array):
                count_array[num_array[i]] = 0
            count_array[num_array[i]] += 1
        return count_array



        
        
        