class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # Return:
    # What exactly am I returning?
        # string length replace k elements 

    # Example:
    # Tiny input + expected output by hand
        # input: aaababb -> 5

    # Brute:
    # Dumb obvious way, even if slow
        # look at every possible substring -> and count number distinct characters

    # Property:
    # What special clue can improve brute force?
    # sorted? BST? contiguous? frequency? top k? level order?
        # it is a continuous window

    # Pattern:
    # sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
        # sliding window with hashmap

    # State:
    # What variables/data structures do I need?
        # freq counter

    # Invariant:
    # What must stay true?
        # window must only contain at most k elements not the most common char

    # Progress:
    # What moves/changes each step?
        # p2 increases in size until 

    # Update:
    # When do I count/save/return answer?
        # count answer after every substring, return after p2 moves to the end


        p1 = 0# initialize p1
        p2 = 0# initialize p2
        freq = {}# initialize freq
        max_freq = 0
        max_length = 0
        # k denotes max number of extra chars allowed
        while p2 < len(s):

            freq[s[p2]] = 1 + freq.get(s[p2], 0) # add current char to freq counter
            if freq[s[p2]] > max_freq:
                max_freq = freq[s[p2]]
            
            substring_length = p2 - p1 + 1
            while substring_length - max_freq  > k: 
                freq[s[p1]] -= 1
                if freq[s[p1]] == 0:
                    del freq[s[p1]]
                p1 += 1
                substring_length = p2 - p1 + 1
            
            max_length = max(max_length, substring_length)
            p2 += 1

        return max_length
            
            # calculate max_length

            


            


