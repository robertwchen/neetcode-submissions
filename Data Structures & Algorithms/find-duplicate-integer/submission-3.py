# []
# [1, 2, 3, 2, 2]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                return num
            nums[num - 1] *= -1
        return None
            
            

                # if so return said number
            # then calculate the value use abs
            # make that index - 1 negative

        