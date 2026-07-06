class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * len(nums)
        left = [1] * len(nums)
        # calculate left product
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
    
        # calculate right product
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res



            

        