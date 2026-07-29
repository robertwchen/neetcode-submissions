class Solution:
    # [1 2 3 4 4]
    #.     s   f
    def findDuplicate(self, nums: List[int]) -> int:
        # look through all numbers
            # check a numbers corresponding indice - 1
        
        slow = nums[0]
        fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now fast == slow
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow