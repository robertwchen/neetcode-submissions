

# [1, 2, 3, 4, 5]
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r < len(nums) - 1:
            # find next bound
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            
            l = r + 1
            r = furthest
            count += 1
        return count
        
