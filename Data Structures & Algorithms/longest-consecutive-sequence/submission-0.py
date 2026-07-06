class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn list into a set
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
        # for all elements in set
            if (num - 1) in nums_set:
                continue
            # check if it is start of sequence (check left neighbor)

            # if a number is a start of sequence
            current_num = num
            current_len = 0
            while current_num in nums_set:
                current_len += 1
                current_num += 1
            max_len = max(current_len, max_len)
        return max_len
                    
        

        