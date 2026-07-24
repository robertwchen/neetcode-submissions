# where am I
    # at some point on the array
# what am I doing
    # keeping track of max product an min product
# what do I return


# [ -1. 3. -4]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        cur_max = 1
        cur_min = 1


        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
                continue
            
            prev_max = cur_max
            cur_max = max(n * cur_max, n * cur_min, n) #[-1, 8]
            cur_min = min(n * prev_max, n * cur_min, n)
            res = max(res, cur_max, cur_min)
        return res




        