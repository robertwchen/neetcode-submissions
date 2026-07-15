class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if high > mid min in left
        # if high < mid min in right
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = ( left + right ) // 2
            if nums[right] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
        return nums[right]
            
        