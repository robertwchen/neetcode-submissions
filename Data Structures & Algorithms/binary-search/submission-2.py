class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Goal: find target in sorted array
        # Store: p1 and p2
        # Valid: while p1 <= p2, if pointers same pick same target 
        # Fix: 
        # Answer

        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            mid = (p2 + p1) // 2
            print(mid)
            if target > nums[mid]:
                p1 = mid + 1

            elif target < nums[mid]:
                p2 = mid - 1

            elif target == nums[mid]:
                return mid
        return -1 

        