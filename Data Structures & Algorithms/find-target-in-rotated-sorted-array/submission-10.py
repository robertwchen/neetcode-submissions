class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # is right sorted or left
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[right]: # right sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1

            elif nums[mid] > nums[right]: # left sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
