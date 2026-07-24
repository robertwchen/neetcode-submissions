# where am I
# what am I doing
# what do I return

# [ 3, 4, 5, 6, 1, 2]

# [6, 1, 2, 3, 4, 5]
#.   p1 p2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] >= nums[hi]:
                lo = mid + 1
        return nums[lo]
             


        