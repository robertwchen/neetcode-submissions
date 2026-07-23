# where am I
    # at some point on array
# what am I doing
    # checking if the previous number exists
# what do I return
    # the longest substring

# brute force: look at every point on array and check if the next one exists incrementing
# or sort the array and lookfor any breaks and take the p1 -> p2 length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_len = 0
        for num in nums:
            curr_len = 0
            while num in nums_set:
                num += 1
                curr_len += 1
            max_len = max(curr_len, max_len) 
        return max_len
            

        