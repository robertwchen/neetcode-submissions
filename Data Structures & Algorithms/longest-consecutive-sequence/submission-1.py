class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Pattern:
        # What algorithm shape is this?
        # set lookup, look for prev

        # State:
        # What does each variable/store object mean?
        # set stores all elements
        # curr_length: tracks current length of sequence
        # max_length: tracks max_length

        # Invariant:
        # What must stay true?
        

        # Progress:
        # What moves/changes every loop or recursive call?
        # the current index will accumulate count

        # Update:
        # When do I count/save/return answer?
        # at the end of a sequence when the next character doesn't exist

        # Return:
        # What type do I return: bool/int/list/node/None?
        # return longest length

        # nums -> set
        nums_set = set(nums)
        max_length = 0
        # loop through each element:
        for n in nums:
            if (n - 1) in nums_set:
                continue
            current_length = 0
            while n in nums_set:
                current_length += 1
                n += 1
            max_length = max(max_length, current_length)
        return max_length
            
            # for each element check if num before exists if so continue

            # initialize current_count
            # look at set if next char there count +1

            # take max of current and max

        
                
        