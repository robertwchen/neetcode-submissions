class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 1, 2]
        # 3, 1], 2]

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[hi] >= nums[mid]:
                hi = mid
            elif nums[hi] < nums[mid]:
                lo = mid + 1

        return nums[lo]

        