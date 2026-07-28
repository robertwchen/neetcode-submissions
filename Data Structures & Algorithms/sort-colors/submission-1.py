class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            elif num == 2:
                count_2 += 1

        i = 0
        for _ in range(count_0):
            nums[i] = 0
            i += 1

        for _ in range(count_1):
            nums[i] = 1
            i += 1
        
        for _ in range(count_2):
            nums[i] = 2
            i += 1