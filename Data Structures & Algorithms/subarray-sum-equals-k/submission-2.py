# so running array
# [ 1 2 3 10]
# [.1.3.6.10]                       # looking for range

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_sums = {0:1} # stores sums up to the variable 
        current_sum = 0

        for i in range(len(nums)):
            num = nums[i]
            current_sum += num
            
            target = current_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]

            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)

        return count

            # check prefix_sums array
            