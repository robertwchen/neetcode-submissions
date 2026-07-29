class Solution:
    # [1 1 2]
    def findDuplicate(self, nums: List[int]) -> int:
        # look through all numbers
            # check a numbers corresponding indice - 1
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                return num  # represents its value
            # mark num as negative
            nums[num - 1] *= -1
        