class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first find the inflection point 
        # so looking at mid
        # if right bigger than mid:
            # if mid <= hi
                # search left
            # else
                # search right

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            print(low, mid, high)

            if nums[mid] < nums[high]: 
                high = mid
            elif nums[mid] >= nums[high]:
                low = mid + 1
        return nums[low]
        