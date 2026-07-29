class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        # so find min size
        min_size = float('inf')
        current_sum = 0
        p1 = 0
        for p2 in range(len(nums)):
            current_sum += nums[p2]

            while current_sum >= target:
                min_size = min(min_size, p2 - p1 + 1)
                current_sum -= nums[p1]
                p1 += 1

        return min_size if min_size != float('inf') else 0