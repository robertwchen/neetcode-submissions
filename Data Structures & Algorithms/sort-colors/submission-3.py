class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1

        cur = 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[p1], nums[cur] = nums[cur], nums[p1]
                cur += 1
                p1 += 1
            elif nums[cur] == 1:
                cur += 1
                
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
                
            

        

# if p1 starts beginning p2 starts at the end
# current starts at beginning

