class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search
        # while p1 < p2:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            #print(left, mid, right)

            if target == nums[mid]:
                return mid

            # check which side is sorted then decide if target in that side
            if nums[left] <= nums[mid]:
                # check if in this side 
                if nums[left] <= target < nums[mid]:
                    # search left side
                    right = mid - 1
                else: 
                    left = mid + 1
                    # search right side

            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    # search right side
                else:
                    right = mid - 1

        return -1